from django.forms import widgets


class DateInput(widgets.DateInput):
    input_type = "date"


class DateTimeInput(widgets.DateTimeInput):
    input_type = "datetime-local"


class TimeInput(widgets.TimeInput):
    input_type = "time"
