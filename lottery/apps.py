from django.apps import AppConfig


class LotteryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'lottery'
    def ready(self) -> None:
        from . import scheduler
        scheduler.start()