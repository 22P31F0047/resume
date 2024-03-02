from django.contrib import admin
from .models import register,update_details,Education,WorkExperience

# Register your models here.
admin.site.register(register)
admin.site.register(update_details)
admin.site.register(Education)
admin.site.register(WorkExperience)