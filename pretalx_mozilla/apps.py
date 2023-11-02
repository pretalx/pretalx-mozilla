from django.apps import AppConfig

from pretalx_mozilla import __version__


class PluginApp(AppConfig):
    name = "pretalx_mozilla"
    verbose_name = "Mozilla"

    class PretalxPluginMeta:
        name = "Mozilla"
        author = "Tobias Kunze"
        description = "Pretalx modifications for Mozilla events"
        visible = True
        version = __version__
        category = "LANGUAGE"

    def ready(self):
        from . import signals  # NOQA
