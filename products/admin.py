from django.contrib import admin
from .models import *


# Custom Admins
class ItemAdmin(admin.ModelAdmin):
    list_display = ['item_name','item_price','created_at']


# Register your models here.
admin.site.register(Item,ItemAdmin)
add homepage tab for the restaurant
add simple errors
delete the errors and print the freshh new code
use the templates and rename the menu items