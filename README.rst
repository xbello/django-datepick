========
Datepick
========

Django-datepick is a Django app to add a date, time and datetime pickers to
your forms.

Install
-------

  Install the app with `pip install django-datepick`.

Usage with forms
----------------

Change the widget used in your forms to use the widgets included in this app::

    from django import forms
    from datepick import widgets

    class MyForm(forms.Form):
        date_field = forms.DateField(widget=widgets.DateInput)
        datetime_field = forms.DateTimeField(widget=widgets.DateTimeInput)
        time_field = forms.TimeField(widget=widgets.TimeInput)

Usage with models
-----------------

Change the field used in your models to use the fields from this app::

    from django.db import models
    from datepick import fields

    class MyDateModel(models.Model):
        d = fields.DateField()
        dt = fields.DateTimeField()
        t = fields.TimeField()
