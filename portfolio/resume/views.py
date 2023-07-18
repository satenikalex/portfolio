from django.shortcuts import render
from .models import (Skill,Education,Experience,Language,New_Skill,SocialLink, Personal_info, Info,Service,Testimonial, Personal)

# Create your views here.


def home(request):
    skills = Skill.objects.all()
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    languages = Language.objects.all()
    New_skills = New_Skill.objects.all()
    social_links = SocialLink.objects.all()
    personal_info = Personal_info.objects.first()
    info = Info.objects.first()
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    Personal = Personal.objects.get(user__username = 'Satenik')

    data = {
        "skills": skills,
        "educations": educations,
        "experiences": experiences,
        "languages": languages,
        "New_skills": New_skills,
        "social_links": social_links,
        "personal_info": personal_info,
        "infi": info,
        "services": services,
        "testimonials": testimonials,

    }

    return render(request, "home.html", context=data)