from django.contrib import admin
from .models import Blog , Category
# Register your models here.
class BlogAdmin(admin.ModelAdmin):
    list_display =['title','jpublish','slug','status','thumbnail']

class CategoryAdmin(admin.ModelAdmin):
    list_display =['title','slug','is_active']

admin.site.register(Blog,BlogAdmin)
admin.site.register(Category,CategoryAdmin)