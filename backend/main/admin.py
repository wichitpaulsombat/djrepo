from django.contrib import admin
from main.models import Company, Resume, Skill, Education, PreviousJob, Rating

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('owner', 'success_summary')

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'resume')

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ('degree', 'school_name', 'resume')

@admin.register(PreviousJob)
class PreviousJobAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'resume')

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('rater', 'resume', 'score', 'created_at')