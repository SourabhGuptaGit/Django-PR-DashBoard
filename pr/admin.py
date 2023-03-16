from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(ALL_Repo)
class All_Repo(admin.ModelAdmin):
    list_display = ('Developer_Email_ID', 'Repo', 'Open_PR', 'Merged_PR', 'Declined_PR')
    ordering = ('Developer_Email_ID',)
    search_fields = ("Developer_Email_ID", "Repo")

@admin.register(HmicSandBox)
class HmicSandBox(admin.ModelAdmin):
    list_display = ('Developer_Email_ID', 'Repo', 'Open_PR', 'Merged_PR', 'Declined_PR')
    ordering = ('Developer_Email_ID',)
    search_fields = ("Developer_Email_ID", "Repo")

@admin.register(FCC)
class FCCadmin(admin.ModelAdmin):
    list_display = ('Developer_Email_ID', 'Repo', 'Open_PR', 'Merged_PR', 'Declined_PR')
    ordering = ('Developer_Email_ID',)
    search_fields = ("Developer_Email_ID", "Repo")

@admin.register(RCC)
class RCCadmin(admin.ModelAdmin):
    list_display = ('Developer_Email_ID', 'Repo', 'Open_PR', 'Merged_PR', 'Declined_PR')
    ordering = ('Developer_Email_ID',)
    search_fields = ("Developer_Email_ID", "Repo")

@admin.register(Rtosapps)
class RtosAppsadmin(admin.ModelAdmin):
    list_display = ('Developer_Email_ID', 'Repo', 'Open_PR', 'Merged_PR', 'Declined_PR')
    ordering = ('Developer_Email_ID',)
    search_fields = ("Developer_Email_ID", "Repo")