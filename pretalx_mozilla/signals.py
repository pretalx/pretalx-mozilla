from django.dispatch import receiver

from pretalx.common.signals import register_locales


@receiver(register_locales)
def register_locales(**kwargs):
    event = kwargs.pop("sender", None)
    if event:
        if "pretalx_mozilla" not in getattr(event, "plugin_list") or []:
            return []
    return ["en-mozilla"]
