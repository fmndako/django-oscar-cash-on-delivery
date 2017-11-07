
====================
COD for django-oscar
====================

Cash on delivery payment module for django-oscar

Installation
------------

* Install: `pip install -e git+https://github.com/michaelkuty/django-oscar-cash-on-delivery#egg=cashondelivery`
* Add ``cashondelivery`` to ``INSTALLED_APPS``
* Add ``cashondelivery`` urls to project urls:

.. code-block:: python

    from cashondelivery.dashboard.app import application as cashon
    
    url(r'^dashboard/cash-on/', include(cashon.urls)),


* Use cashondelivery checkout app:

.. code-block:: python

    # file: <project>/checkout/app.py -- forked checkout app

    # replace default checkout app with cashondelivery app
    from oscar.apps.checkout import app
    from cashondelivery.app import application as checkout_app

    app.application = checkout_app

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
