from django.conf import settings
from django.contrib import admin

from django.contrib.auth import get_user_model
 
from django.contrib.auth.admin import UserAdmin
from django.forms import Textarea
from accounts.models import CustomUser


class UserAdminConfig(UserAdmin):
    # this import for the styling the feilds

    model = CustomUser

    # based on this search it give the table row
    search_fields = ('email','user_name','first_name','last_name')

    # for ordering the rows objects in admin panel
    ordering = ('-start_date',)

    # which feilds need to show to the user
    list_display = ('email','user_name','start_date','first_name','is_active','is_staff')

    # list of filter that shown in the right side of the admin panel 

    list_filter = ('first_name','email','first_name','is_active','is_staff')

    # this is set to the user individuals displaying
    fieldsets = (
        (None,{'fields':('email','first_name','user_name',)}),
        ('Permission',{'fields':('is_active','is_staff')}),
        ('Personal',{'fields':('about',)})
    )
    # this is used to styling the form feild in the adming panel 

    formfield_overrides = {
        CustomUser.about : {'widget': Textarea(attrs={'rows': 2 , 'cols':40})},
    }
    add_fieldsets = (
        ('PLEASE ENTER YOUR CREDENTIALS ',{'classes':('wide',),'fields':('email','user_name','password1','password2','first_name')}),
    )

    






admin.site.register(get_user_model(),UserAdminConfig)

# Register your models here.
