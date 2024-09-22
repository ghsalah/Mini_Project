from django.apps import AppConfig

class User1Config(AppConfig):
    name = 'user_1'

    def ready(self):
        import user_1.signals
