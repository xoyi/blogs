from django.contrib import admin
from .models import BookInfo,HeroInfo
# Register your models here.
class HeroInfoLine(admin.TabularInline):
    model = HeroInfo
    extra = 5
class BookInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'btitle', 'creat_time', 'update_time']
    search_fields = ['btitle']
    list_filter = ['btitle']
    fieldsets = [
        ('base', {'fields': ['btitle']}),
        ('super', {'fields': ['creat_time']})
    ]
    inlines = [HeroInfoLine]
admin.site.register(BookInfo,  BookInfoAdmin)
admin.site.register(HeroInfo)