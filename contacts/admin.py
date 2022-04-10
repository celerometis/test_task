from django.contrib import admin
from .models import Contact
# Register your models here.


@admin.register(Contact)
class PeriodAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
    list_per_page = 25