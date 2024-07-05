from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Homepage)
admin.site.register(Statistic)

class NewsDetailInline(admin.TabularInline):
    model = NewsDetail
    extra = 1

class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsDetailInline]

class Requirementsinline(admin.TabularInline):
    model = Requirement
    extra = 1

class RequirementAdmin(admin.ModelAdmin):
    inlines = [Requirementsinline]

admin.site.register(News, NewsAdmin)
admin.site.register(Raw_material)
admin.site.register(Team_Member)
admin.site.register(Certificates)
admin.site.register(Career)
admin.site.register(Announcement,RequirementAdmin)
admin.site.register(Requirement)