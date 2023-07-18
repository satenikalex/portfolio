from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, URLValidator, EmailValidator
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.

class Personal_info(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=25)
    phone = models.CharField(max_length=15)
    email = models.EmailField(validators=[EmailValidator])
    city = models.CharField(max_length=40)
    age = models.PositiveIntegerField()
    degree = models.CharField(max_length=20)
    freelance = models.CharField(max_length=20)
    github = models.URLField(validators=[URLValidator])
    sumary_name = models.CharField(max_length=30)
    sumary_description = models.TextField(max_length=300)
    about = models.TextField(max_length=300, blank=True, null=True)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.phone}, {self.email}, {self.city}, {self.age}, {self.degree}, {self.freelance}, {self.github}"


class Info(models.Model):
    happy_clients_count = models.PositiveIntegerField()
    happy_clients_description = models.TextField(max_length=250, blank=True, null=True)
    
    projects_count = models.PositiveIntegerField()
    projects_description = models.TextField(max_length=250, blank=True, null=True)
    
    awards_count = models.PositiveIntegerField()
    awards_description = models.TextField(max_length=250, blank=True, null=True)
    
    coffee_cup_count = models.PositiveIntegerField()
    coffee_cup_description = models.TextField(max_length=10000, blank=True, null=True )
    
    created_on = models.DateTimeField(auto_now=True)


class Skill(models.Model):
    name = models.CharField(max_length=20)
    value = models.PositiveIntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} skill value is {self.value}"


class Education(models.Model):
    university_name = models.TextField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    grade = models.TextField(max_length=100, blank=True, null=True)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.university_name}, {self.grade}"


class Experience(models.Model):
    job_title = models.TextField(max_length=50)
    company_name = models.TextField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    job_discribtion = models.TextField(max_length=300, blank=True, null=True)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.company_name}, {self.job_title}"


class Language(models.Model):
    name = models.CharField(max_length=20)
    level = models.CharField(max_length=20)
    
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.level}"


class New_Skill(models.Model):
    name = models.CharField(max_length=50)
    
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"


class SocialLink(models.Model):
    link = models.URLField()
    link_name = models.CharField(max_length=20)
   
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.link_name}"


class Service(models.Model):
    service_name = models.CharField(max_length=20)
    service_description = models.TextField(max_length=200)
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.service_name}"


class Testimonial(models.Model):
    name = models.CharField(max_length=50)
    job_position = models.CharField(max_length=50)
    opinion = models.CharField(max_length=300)
    image = models.ImageField()
    created_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}, {self.job_position}, {self.created_on}"

class Personal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)