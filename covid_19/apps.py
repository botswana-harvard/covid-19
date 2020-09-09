from django.apps import AppConfig as DjangoAppConfig

from edc_base.apps import AppConfig as BaseEdcBaseAppConfig


class AppConfig(DjangoAppConfig):
    name = 'covid_19'
    verbose_name = 'Covid-19'


class EdcBaseAppConfig(BaseEdcBaseAppConfig):
    project_name = 'BHP C19-R'
    institution = 'Botswana-Harvard AIDS Institute'
