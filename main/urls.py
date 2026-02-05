from django.urls import path
from main import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('resumes/', views.resume_list, name='resume_list'),
    path('resume/<int:pk>/', views.resume_detail, name='resume_detail'),
    path('resume/edit/', views.edit_resume, name='edit_resume'),
    path('resume/<int:pk>/rate/', views.rate_resume, name='rate_resume'),
    path('resume/edit/add-skill/', views.add_skill, name='add_skill'),
    path('resume/edit/add-education/', views.add_education, name='add_education'),
    path('resume/edit/add-job/', views.add_job, name='add_job'),
]