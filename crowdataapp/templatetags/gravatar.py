from django import template
import hashlib

register = template.Library()

@register.filter(name='gravatar')
def gravatar_url_string(value):
    return 'http://www.gravatar.com/avatar/' + hashlib.md5(value).hexdigest()
