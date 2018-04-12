from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

from cashondelivery import models


class TransactionListView(ListView):
    model = models.CashOnDeliveryTransaction
    context_object_name = 'transactions'
    template_name = 'dashboard/cashondelivery/transaction_list.html'


class TransactionDetailView(DetailView):
    model = models.CashOnDeliveryTransaction
    context_object_name = 'txn'
    template_name = 'dashboard/cashondelivery/transaction_detail.html'

    def post(self, request, *args, **kwargs):
        txn = self.get_object()
        if txn.confirm():
            messages.success(self.request, _("Cash collection confirmed"))
        else:
            messages.warn(self.request, _("Already confirmed as collected"))
        return HttpResponseRedirect(
            reverse('cashondelivery-transaction-detail',
                    kwargs={'pk': txn.pk}))
