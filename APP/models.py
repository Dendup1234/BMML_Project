from django.db import models

# Create your models here.
class Homepage(models.Model):
    hero_title = models.CharField(max_length=200)
    hero_image = models.ImageField(upload_to='image/')
    home_image = models.ImageField(upload_to='image/')
    def __str__ (self):
        return self.hero_title

class Statistic(models.Model):
    established = models.CharField(max_length=200)
    client = models.CharField(max_length=200)
    production_hour = models.CharField(max_length=200)
    production_day = models.CharField(max_length=200)
    production_year = models.CharField(max_length=200)

    def __str__ (self):
        return f'statistic'

class Raw_material(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='image/')

    def __str__ (self):
        return self.name

class Team_Member(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    phone = models.IntegerField(blank=True,null=True)
    image = models.ImageField(upload_to='image/')
    facebook = models.URLField(max_length=200,blank=True,null=True)
    email = models.EmailField(max_length=300,blank=True,null=True)
    linkedin = models.URLField(max_length=200, blank=True, null=True)

    def __str__ (self):
        return self.name

class Certificates(models.Model):
    image = models.ImageField(upload_to='image/')
    def __str__ (self):
        return  f"Certificates"

class Career(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='image/')

    def __str__ (self):
        return self.title

class Announcement(models.Model):
    announcement = models.CharField(max_length=200)
    image = models.ImageField(upload_to='image/',blank=True,null=True)
    date = models.DateField(auto_now_add=True)
    hiring_process = models.TextField()
    descriptions = models.TextField(blank=True,null=True)
    def __str__ (self):
        return self.announcement

class Requirement(models.Model):
    announcement = models.ForeignKey(Announcement,related_name='requirement',on_delete= models.CASCADE)
    requirement = models.CharField(max_length=200)

    def __str__ (self):
        return f'requirement for {self.announcement.announcement}'

class Reports(models.Model):
    title = models.CharField(max_length=255)
    upload = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.title

class Tenders(models.Model):
    title = models.CharField(max_length=255)
    upload = models.FileField(upload_to='uploads/')

    def __str__(self):
        return self.title

class Annual_Audited_Reports(models.Model):
    title = models.CharField(max_length=255)
    upload = models.FileField(upload_to='uploads/')
    def __str__(self):
        return self.title



class Admin_info(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=300,blank=True,null=True)
    facebook = models.URLField(max_length=200,blank=True,null=True)
    location = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    linkedin = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name

class Certificates_about(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/',blank=True,null=True)
    def __str__(self):
        return self.name

