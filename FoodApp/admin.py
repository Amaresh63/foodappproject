from django.contrib import admin
from FoodApp.models import Item
from users.models import Profile
# Register your models here.

admin.site.register(Item)
admin.site.register(Profile)