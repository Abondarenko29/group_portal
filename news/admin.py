from django.contrib import admin
from news.models import News, Project, FileModel


# Register your models here.
admin.site.register(News)
admin.site.register(Project)
admin.site.register(FileModel)
