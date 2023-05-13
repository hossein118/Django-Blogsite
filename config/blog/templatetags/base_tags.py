from django import template
from blog.models import Category

register = template.Library()

@register.simple_tag()
def hello():
    return "وبلاگ جنگویی من "


@register.inclusion_tag('temptags/category_navber.html')
def navbar():
    categories = Category.objects.filter(is_active=True)
    return {'categories':categories}