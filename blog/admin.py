from django.contrib import admin
from . import models

# Register your models here.

my_model=[models.Post]
admin.site.register(my_model)