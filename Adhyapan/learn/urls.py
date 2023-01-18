from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from learn import views
from django.views.generic.base import RedirectView
urlpatterns = [ 
    path('home/', views.HomeView.as_view()),
    path('about/', views.AboutView.as_view()),
    path('contact/', views.ContactView.as_view()),

    path('video/', views.VideoListView.as_view()),
    path('video/<int:pk>', views.VideoDetailView.as_view()),    

    path('notes/', views.NotesListView.as_view()),
    path('notes/<int:pk>', views.NotesDetailView.as_view()),    

    path('question/', views.QuestionListView.as_view()),
    path('question/<int:pk>', views.QuestionDetailView.as_view()),        
    path('question/create/', views.QuestionCreate.as_view(success_url="/learn/question")),
    
    path('contact/submit', views.contact),
    
    path('', RedirectView.as_view(url="home/")),    
]
