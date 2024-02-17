from django.db import models
from django.contrib import admin
from testapp.models import User,Profile,VideoData
# Register your models here.
class VideoDataModel(admin.ModelAdmin):
    list_display = ('video_file',)
admin.site.register(User)
admin.site.register(Profile)

admin.site.register(VideoData,VideoDataModel)