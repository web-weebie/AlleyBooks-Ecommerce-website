from django.contrib import admin
from .models import Users, Profile


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'is_active', 'is_superuser', 'is_staff', 'password', 'last_login']
    list_display_links = ['email']


admin.site.register(Users, UserAdmin)



class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'id', 'username', 'fullname', 'birthday', 'created_time', 'slug']
    list_display_links = ['username']

    prepopulated_fields = {"slug": ("username",)}


admin.site.register(Profile, ProfileAdmin)