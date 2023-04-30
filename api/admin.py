from django.contrib import admin
from .models import MyUser,Blog,Comments

# Register your models here.


admin.site.register(MyUser)
admin.site.register(Blog)
admin.site.register(Comments)