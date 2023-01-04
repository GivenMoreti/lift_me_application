from django.contrib import admin

# Register your models here.

from .models import Lift



class LiftAdmin(admin.ModelAdmin):

    list_display = ('username','first_name','last_name','from_location','to_location','leaving_with','date_time_of_leaving','number_of_bags','estimated_kms','willing_to_pay')


admin.site.register(Lift,LiftAdmin)
