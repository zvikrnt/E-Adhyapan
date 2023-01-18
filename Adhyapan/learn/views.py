from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from learn.models import MyVideo, MyProfile, Notes, Question, Topic, VideoLike
from django.db.models import Q
from django.views.generic.detail import DetailView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.http.response import HttpResponseRedirect
from django.core.mail import send_mail
# Create your views here.

def contact(req):
    sub = "Adhyapan Contact :: %s " % req.POST.get("uname")
    body = "Phone No = %s\nEMail = %s\nMessage = %s " % (req.POST.get("phone_no"), req.POST.get("email"),  req.POST.get("msg"))
    send_mail(
        sub,
        body,
        req.POST.get("email"),
        ['aloya.effcon@gmail.com'],
        fail_silently=False,
    )
    return HttpResponseRedirect("/learn/home?msg=Submited Successfully")



class HomeView(TemplateView):
    template_name = "learn/home.html"
    def get_context_data(self, **kwargs):
        context = TemplateView.get_context_data(self, **kwargs)
        context["videos"] = MyVideo.objects.all().order_by('-id')[:6];
        return context;
    

class AboutView(TemplateView):
    template_name = "learn/about.html"

class ContactView(TemplateView):
    template_name = "learn/contact.html"


class VideoListView(ListView):
    model = MyVideo
    def get_queryset(self):
        si = self.request.GET.get("si")
        if si == None:
            si = ""
        return MyVideo.objects.filter(Q(title__icontains = si)| Q(description__icontains = si)).order_by("-id")
             
 
class VideoDetailView(DetailView):
    model = MyVideo


class NotesListView(ListView):
    model = Notes
    def get_queryset(self):
        si = self.request.GET.get("si")
        if si == None:
            si = ""
        return Notes.objects.filter(Q(subject__icontains = si)| Q(description__icontains = si)).order_by("-id")
             
 
class NotesDetailView(DetailView):
    model = Notes

@method_decorator(login_required, name="dispatch")    
class QuestionCreate(CreateView):
    model = Question
    fields = ["subject", "topic", "question"]
    def form_valid(self, form):
        self.object = form.save()
        self.object.asked_by = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class QuestionListView(ListView):
    model = Question
    def get_queryset(self):
        si = self.request.GET.get("si")
        if si == None:
            si = ""
        return Question.objects.filter(Q(subject__icontains = si)| Q(topic__name__icontains = si)).order_by("-id")
             
 
class QuestionDetailView(DetailView):
    model = Question



#     
# @method_decorator(login_required, name="dispatch")    
# class ProfileUpdate(UpdateView):
#     model = Profile
#     fields = ["branch", "sem", "marks_10", "marks_12", "marks_aggr", "rn", "phone_no", "email", "skills", "myimg", "myresume"]
# 
# 
# 
# @method_decorator(login_required, name='dispatch')
# class MyList(TemplateView):
#     template_name = "college/mylist.html"
#     def get_context_data(self, **kwargs):
#         context = TemplateView.get_context_data(self, **kwargs)
#         context["notices"] = Notice.objects.all().order_by('-id')[:3];
#         context["questions"] = Question.objects.all().order_by('-id')[:3];
#         return context;

