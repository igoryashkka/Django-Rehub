from django import template
from women.models import *

register = template.Library()

@register.simple_tag(name = 'getcats')
def get_cat():
    categories = Category.objects.all()
    return categories

@register.inclusion_tag('women/list_cat.html')
def show_cat():
    categories = Category.objects.all()
    return {'cats': categories}