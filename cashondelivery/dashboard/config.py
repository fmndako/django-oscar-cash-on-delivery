from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class DashboardConfig(AppConfig):
    label = 'cashondelivery_dashboard'
    name = 'cashondelivery.dashboard'
    verbose_name = _('Cash On Delivery Dashboard')
