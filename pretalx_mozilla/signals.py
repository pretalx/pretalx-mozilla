from django.dispatch import receiver
from django.template.loader import get_template
from pretalx.common.signals import register_locales
from pretalx.orga.signals import html_head


@receiver(register_locales)
def register_locales(**kwargs):
    event = kwargs.pop("sender", None)
    if event:
        if "pretalx_mozilla" not in getattr(event, "plugin_list", None) or []:
            return []
    return ["en-mozilla"]


@receiver(html_head, dispatch_uid="mozilla_html_head")
def add_stylesheet(sender, request, **kwargs):
    if "en-mozilla" not in request.event.locales:
        return ""
    template = get_template("pretalx_mozilla/style.html")
    return template.render()
