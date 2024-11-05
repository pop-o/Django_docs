from django.contrib import admin
from .models import Question,Choice

#to display in the admin page
admin.site.register(Question)
admin.site.register(Choice)