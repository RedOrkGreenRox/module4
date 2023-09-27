from django.contrib import admin
from .models import Advertisement
from django.utils.html import format_html


class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'img', 'price', 'created_date', 'updated_date', 'auction']
    list_filter = ['price', 'created_at', 'auction']
    actions = ['make_auction_as_false', 'make_auction_as_true']
    fieldsets = (
        ('Общее', {
            'fields': ('title', 'description', 'image')
        }),
        ('Финансы', {
            'fields': ('price', 'auction'),
            'classes': ['collapse']
        })
    )

    @admin.action(description='Убрать возможность торга')
    def make_auction_as_false(self, request, queryset):
        queryset.update(auction=False)

    @admin.action(description='Добавить возможность торга')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

    @admin.display(description='Изображение')
    def img(self, obj):
        return format_html(f'<img src="{obj.image.url if obj.image else "../../../static/img/adv.png"}" '
                           f'style="max-width:100px; max-height:100px"/>')


admin.site.register(Advertisement, AdvertisementAdmin)
