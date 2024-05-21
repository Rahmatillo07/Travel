from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Ticket,Company,Category

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['id','category','company','name','get_image','comfort','time','price']
    list_display_links = ['name']
    list_filter = ['category','name']
    list_editable = ['category','price']

    def get_image(self, obj):
        return mark_safe(f'<img src="{obj.image.url if obj.image else None}" width="75">')


admin.site.register(Company)
admin.site.register(Category)


# Register your models here.
