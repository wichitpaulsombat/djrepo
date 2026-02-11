from django.urls import path
from rest_framework.routers import DefaultRouter
from main.views import *

router = DefaultRouter()
router.register(r'resumes', ResumeViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'educations', EducationViewSet)
router.register(r'experiences', ExperienceViewSet)
router.register(r'contacts', ContactViewSet)
router.register(r'profiles', ProfileViewSet)

urlpatterns = [
    #path('', landing_page, name='landing_page'),
    path('', include(router.urls)),
]

