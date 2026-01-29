from django.contrib import admin

from main.models import Company, PreviousJob

# Register your models here.
admin.site.register(PreviousJob)
admin.site.register(Company)