from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import CustomUser


# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = CustomUser
    readonly_fields = ["date_joined"]
    list_display = ['pk', 'email', 'username', 'first_name', 'last_name']
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('email', 'first_name', 'last_name', 'date_of_birth', 'address1',
         'zip_code', 'city', 'country', 'mobile_phone', 'photo', 'date_joined')}),
    )
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'address1',  'zip_code',
         'city', 'country', 'mobile_phone', 'photo',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
