from django.apps import AppConfig
# from django.apps import 

class AccountConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'account'
    def ready(self):
        # import signal handlers
        import images.signals