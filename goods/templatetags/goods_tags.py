from django import template

from goods.models import Categoreis


register = template.Library()


@register.simple_tag
def tag_categories():
    return Categoreis.objects.all()

