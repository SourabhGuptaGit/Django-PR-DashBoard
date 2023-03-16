from django.db import models
from datetime import datetime

# Create your models here.

class ALL_Repo(models.Model):

    index = models.IntegerField('repos_index', primary_key=True)
    Developer_Email_ID = models.EmailField('repos_email')
    Repo = models.CharField('repos_Repo', max_length=20)
    Last_Merge_Branch = models.CharField('repos_merge_branch', max_length=20)
    Open_PR = models.IntegerField('repos_open_pr')
    Merged_PR = models.IntegerField('repos_close_pr')
    Declined_PR = models.IntegerField('repos_decline_pr')
    Open_PR_DateTime = models.TextField('repos open date time')
    Close_PR_DateTime = models.TextField('repos close date time')
    Declined_PR_DateTime = models.TextField('repos decline date time')
    Ages_of_Open_PR = models.TextField(blank=False)
    Ages_of_Close_PR = models.TextField(blank=False)

    def __str__(self):
        return self.Developer_Email_ID
class HmicSandBox(models.Model):

    index = models.IntegerField('hmicsandbox_index', primary_key=True)
    Developer_Email_ID = models.EmailField('hmicsandbox_email')
    Repo = models.CharField('hmicsandbox_Repo', max_length=20)
    Last_Merge_Branch = models.CharField('hmicsandbox_merge_branch', max_length=20)
    Open_PR = models.IntegerField('hmicsandbox_open_pr')
    Merged_PR = models.IntegerField('hmicsandbox_close_pr')
    Declined_PR = models.IntegerField('hmicsandbox_decline_pr')
    Open_PR_DateTime = models.TextField('hmicsandbox open date time')
    Close_PR_DateTime = models.TextField('hmicsandbox close date time')
    Declined_PR_DateTime = models.TextField('hmicsandbox decline date time')
    Ages_of_Open_PR = models.TextField(blank=False)
    Ages_of_Close_PR = models.TextField(blank=False)


    def __str__(self):
        return self.Developer_Email_ID
    
class FCC(models.Model):

    index = models.IntegerField('fcc_index', primary_key=True)
    Developer_Email_ID = models.EmailField('fcc_email')
    Repo = models.CharField('fcc_Repo', max_length=20)
    Last_Merge_Branch = models.CharField('fcc_merge_branch', max_length=20)
    Open_PR = models.IntegerField('fcc_open_pr')
    Merged_PR = models.IntegerField('fcc_close_pr')
    Declined_PR = models.IntegerField('fcc_decline_pr')
    Open_PR_DateTime = models.TextField('fcc open date time')
    Close_PR_DateTime = models.TextField('fcc close date time')
    Declined_PR_DateTime = models.TextField('fcc decline date time')
    Ages_of_Open_PR = models.TextField(blank=False)
    Ages_of_Close_PR = models.TextField(blank=False)


    def __str__(self):
        return self.Developer_Email_ID
    
class RCC(models.Model):

    index = models.IntegerField('rcc_index', primary_key=True)
    Developer_Email_ID = models.EmailField('rcc_email')
    Repo = models.CharField('rcc_Repo', max_length=20)
    Last_Merge_Branch = models.CharField('rcc_merge_branch', max_length=20)
    Open_PR = models.IntegerField('rcc_open_pr')
    Merged_PR = models.IntegerField('rcc_close_pr')
    Declined_PR = models.IntegerField('rcc_decline_pr')
    Open_PR_DateTime = models.TextField('rcc open date time')
    Close_PR_DateTime = models.TextField('rcc close date time')
    Declined_PR_DateTime = models.TextField('rcc decline date time')
    Ages_of_Open_PR = models.TextField(blank=False)
    Ages_of_Close_PR = models.TextField(blank=False)



    def __str__(self):
        return self.Developer_Email_ID
    
class Rtosapps(models.Model):

    index = models.IntegerField('rtosapp_index', primary_key=True)
    Developer_Email_ID = models.EmailField('rtosapp_email')
    Repo = models.CharField('rtosapp_Repo', max_length=20)
    Last_Merge_Branch = models.CharField('rtosapp_merge_branch', max_length=20)
    Open_PR = models.IntegerField('rtosapp_open_pr')
    Merged_PR = models.IntegerField('rtosapp_close_pr')
    Declined_PR = models.IntegerField('rtosapp_decline_pr')
    Open_PR_DateTime = models.TextField('rtosapp open date time')
    Close_PR_DateTime = models.TextField('rtosapp close date time')
    Declined_PR_DateTime = models.TextField('rtosapp decline date time')
    Ages_of_Open_PR = models.TextField(blank=False)
    Ages_of_Close_PR = models.TextField(blank=False)


    def __str__(self):
        return self.Developer_Email_ID
    