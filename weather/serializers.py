from rest_framework import serializers
from .models import WeatherReport

class GetWetherReportSerializer(serializers.ModelSerializer):
	class Meta:
		model =WeatherReport
		fields = ('year','month','value')











