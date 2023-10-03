from django.apps import AppConfig


class PluginApp(AppConfig):
    name = "pretalx_mozilla"
    verbose_name = "Mozilla"

    class PretalxPluginMeta:
        name = "Mozilla"
        author = "Tobias Kunze"
        description = "Pretalx modifications for Mozilla events"
        visible = True
        version = "0.0.0"
        category = "LANGUAGE"

    def ready(self):
        from . import signals  # NOQA
