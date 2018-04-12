
====================
COD for django-oscar
====================

Cash on delivery payment module for django-oscar

Installation
------------

* Install: ``pip install -e git+https://github.com/michaelkuty/django-oscar-cash-on-delivery#egg=cashondelivery``
* Add ``cashondelivery`` to ``INSTALLED_APPS``
* Add ``cashondelivery`` urls to project urls:

.. code-block:: python

    from cashondelivery.dashboard.app import application as cod_app
    
    url(r'^dashboard/cod/', include(cod_app.urls)),

* Add cashondelivery to dashboard navigation:

.. code-block:: python

    # settings
    OSCAR_DASHBOARD_NAVIGATION = [
        ...
        {
            'label': _('Fulfilment'),
            'icon': 'icon-shopping-cart',
            'children': [
                ...
                {
                    'label': _('COD transactions'),
                    'url_name': 'cashondelivery-transaction-list',
                },
                ...
        ...

* Use cashondelivery checkout app:

.. code-block:: python

    # file: <project>/checkout/app.py -- forked checkout app

    # replace default checkout app with cashondelivery app
    from oscar.apps.checkout import app
    from cashondelivery.app import application as cod_app

    app.application = cod_app

* Or fork ``django-oscar`` checkout app and use ``PaymentDetailsView`` from ``sandbox/checkout/views.py``:

.. code-block:: python

    # your checkout/app.py
    from oscar.apps.checkout import app
    from .views import PaymentDetailsView

    class CheckoutApplication(app.CheckoutApplication):
        payment_details_view = PaymentDetailsView


    application = CheckoutApplication()

