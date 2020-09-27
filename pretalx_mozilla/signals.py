from django.dispatch import receiver

from pretalx.common.signals import register_locales


@receiver(register_locales)
def register_locales(**kwargs):
    return ["en-mozilla"]
