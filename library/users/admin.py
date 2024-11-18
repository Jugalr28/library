from django.contrib import admin
from users.models import User,CustomUser
admin.site.register(User)
admin.site.register(CustomUser)
