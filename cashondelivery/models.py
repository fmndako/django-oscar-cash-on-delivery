import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


def _make_uuid():
    return str(uuid.uuid4())


class CashOnDeliveryTransaction(models.Model):
    order_number = models.CharField(_('Order Number'), max_length=128)
    date_created = models.DateTimeField(_('Date Created'), auto_now_add=True)
    amount = models.DecimalField(
        _('Amount'), max_digits=12, decimal_places=2, null=True, blank=True)
    currency = models.CharField(
        _('Currency'), max_length=8, null=True, blank=True)
    reference = models.CharField(
        _('Reference'), max_length=100, blank=True, unique=True, default=_make_uuid)
    confirmed = models.BooleanField(_('Confirmed'), default=False)
    date_confirmed = models.DateTimeField(_('Date Confirmed'), auto_now=True)

    class Meta:
        ordering = ('-date_created',)
        app_label = 'cashondelivery'
        verbose_name = _('Cash on Delivery')

    @property
    def method(self):
        return _('Cash on Delivery')

    def _as_table(self, params):
        rows = []
        for k, v in sorted(params.items()):
            rows.append('<tr><th>%s</th><td>%s</td></tr>' % (k, v[0]))
        return '<table>%s</table>' % ''.join(rows)

    def __unicode__(self):
        return u'method: %s: amount: %s %s' % (
            self.method, self.amount, self.currency)

    def confirm(self, save=True):
        if not self.confirmed:
            self.confirmed = True
            self.save() # date_confirmed gets set automatically
            return True
