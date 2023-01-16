import django
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.translation import gettext_lazy as _
from django.urls import path
from oscar.core.loading import get_class
from oscar.core.application import OscarDashboardConfig


class CashOnDeliveryDashboardConfig(OscarDashboardConfig):
    name = 'cashondelivery.dashboard'
    label = 'cashondelivery_dashboard'

    namespace = 'cashondelivery_dashboard'

    default_permissions = ['is_staff']

    def ready(self):
        self.cashondelivery_list_view = get_class('cashondelivery_dashboard.views', 'TransactionListView')
        self.cashondelivery_detail_view = get_class('cashondelivery_dashboard.views', 'TransactionDetailView')

    def get_urls(self):
        urls = [
            path('transactions/',  self.cashondelivery_list_view.as_view(), name='cashondelivery-transaction-list'),
            path('transactions/<int:pk>/', self.cashondelivery_detail_view.as_view(), name='cashondelivery-transaction-detail'),
        ]
        return self.post_process_urls(urls)
