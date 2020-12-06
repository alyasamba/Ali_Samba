from django.apps import AppConfig


class BaseConfig(AppConfig):
    name = 'ali'

    def ready(self):
    	import ali.signals
