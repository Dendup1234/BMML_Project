from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Homepage)
admin.site.register(Statistic)

class Requirementsinline(admin.TabularInline):
    model = Requirement
    extra = 1

class RequirementAdmin(admin.ModelAdmin):
    inlines = [Requirementsinline]

admin.site.register(Raw_material)
admin.site.register(Team_Member)
admin.site.register(Certificates)
admin.site.register(Career)
admin.site.register(Announcement,RequirementAdmin)
admin.site.register(Requirement)
admin.site.register(Reports)
admin.site.register(Tenders)
admin.site.register(Admin_info)
admin.site.register(Annual_Audited_Reports)
admin.site.register(Certificates_about)