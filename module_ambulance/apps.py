from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig


class ModuleAmbulanceConfig(AppConfig):
    name = 'module_ambulance'
    verbose_name = _('Registros de la ambulancia')

    label = 'ambulance'
