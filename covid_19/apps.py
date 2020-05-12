from django.apps import AppConfig as DjangoAppConfig

from edc_base.apps import AppConfig as BaseEdcBaseAppConfig


class AppConfig(DjangoAppConfig):
    name = 'covid_19'
    verbose_name = 'Covid-19'


class EdcBaseAppConfig(BaseEdcBaseAppConfig):
    project_name = 'BHP Covid-19 Register'
    institution = 'Botswana-Harvard AIDS Institute'
