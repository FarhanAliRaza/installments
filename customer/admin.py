from django.contrib import admin

# Register your models here.
from .models import Customer, Item , Plan, Month, Total, Account
admin.site.register(Item)
admin.site.register(Plan)
admin.site.register(Month)
admin.site.register(Customer)
admin.site.register(Total)
admin.site.register(Account)