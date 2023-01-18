from django.contrib import admin
from learn.models import MyProfile, MyVideo, Notes, Question, Topic, VideoLike
from django.contrib.admin.options import ModelAdmin

# Register your models here.

admin.site.register(Topic)

class MyProfileAdmin(ModelAdmin):
    search_fields = ["user"]
admin.site.register(MyProfile, MyProfileAdmin)


class MyVideoAdmin(ModelAdmin):
    list_display = ["title", "topic"]
    search_fields = ["title", "description", "uploaded_by"]
    list_filter = ["cr_date", "topic"]
admin.site.register(MyVideo, MyVideoAdmin)

class NotesAdmin(ModelAdmin):
    list_display = ["subject", "topic"]
    search_fields = ["subject", "description", "topic"]
    list_filter = ["uploaded_by", "topic"]
admin.site.register(Notes, NotesAdmin)

class QuestionAdmin(ModelAdmin):
    list_display = ["subject", "topic"]
    search_fields = ["subject", "question", "answer"]
    list_filter = ["topic", "cr_date"]
admin.site.register(Question, QuestionAdmin)

class VideoLikeAdmin(ModelAdmin):
    list_display =  ["video", "liked_by"]
    search_fields = ["video", "liked_by"]
    list_filter = ["video", "liked_by"]
admin.site.register(VideoLike, VideoLikeAdmin)




