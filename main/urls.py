from django.urls import path
from main.views import landing_page


urlpatterns = [
    path('', landing_page, name='landing_page'),
]