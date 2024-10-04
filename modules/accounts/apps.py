from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'modules.accounts'
    verbose_name = 'Акаунты'

    def ready(self):
        import modules.accounts.signals
