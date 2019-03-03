from django.contrib import admin
from django.conf.urls import url,include
from weather.views import GetWetherReport

from rest_framework import routers

app_name='weather'

router = routers.DefaultRouter()


urlpatterns = [
	url(r'^api/',GetWetherReport.as_view()),
    url(r'^', include(router.urls)),
]