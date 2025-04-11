from django import template

register = template.Library()

@register.simple_tag
def absolute_url(request, image_url):
    """Returns the absolute URL for an image."""
    if image_url and request:
        return request.build_absolute_uri(image_url)
    return image_url  # Fallback if request is missing
