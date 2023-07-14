from django.contrib import admin
from .models import Education, New_Skill, Experience, Language, SocialLink, Personal_info, Info, Service, Testimonial, Skill




class SkillAdmin(admin.ModelAdmin):
    list_display = ["name", "value", "created_on"]
    list_filter = ["value"]
    search_fields = ["name"]


class Personal_infoAdmin(admin.ModelAdmin):
    list_display = ["first_name", "last_name",
                    "phone", "email", "city", "created_on"]


class EducationAdmin(admin.ModelAdmin):
    list_display = ["university_name", "start_date",
                    "end_date", "grade", "created_on"]


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ["job_title", "company_name",
                    "start_date", "end_date", "created_on"]


class LanguageAdmin(admin.ModelAdmin):
    list_display = ["name", "level", "created_on"]


class New_SkillAdmin(admin.ModelAdmin):
    list_display = ["name", "created_on"]


class InfoAdmin(admin.ModelAdmin):
    list_display = ["happy_clients_count", "projects_count",
                    "awards_count", "coffee_cup_count", "created_on"]


class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ["link_name", "link", "created_on"]


class ServicekAdmin(admin.ModelAdmin):
    list_display = ["service_name", "created_on"]


class TestimonialAdmin(admin.ModelAdmin):
    list_display = ["name", "job_position", "created_on"]


# Register your models here.
admin.site.register(Skill, SkillAdmin)
admin.site.register(Personal_info, Personal_infoAdmin)
admin.site.register(Education, EducationAdmin)
admin.site.register(Experience, ExperienceAdmin)
admin.site.register(New_Skill, New_SkillAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Info, InfoAdmin)
admin.site.register(SocialLink, SocialLinkAdmin)
admin.site.register(Service, ServicekAdmin)
admin.site.register(Testimonial, TestimonialAdmin)


