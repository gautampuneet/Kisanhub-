from __future__ import unicode_literals

from django.contrib import admin
from weather.models import Country,Metric,WeatherReport


admin.site.register(Country)
admin.site.register(Metric)
admin.site.register(WeatherReport)