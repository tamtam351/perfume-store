from django.contrib import admin
from django.utils.html import format_html
from .models import Perfume

class PerfumeAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image_link','description')  # Changed 'image_preview' to 'image_link'
    search_fields = ('name',)
    list_filter = ('price',)

    def image_link(self, obj):
        if obj.image:
            return format_html('<a href="{}" target="_blank">View Image</a>', obj.image.url)
        return "No Image"

    image_link.short_description = "Image Link"

admin.site.register(Perfume, PerfumeAdmin)
