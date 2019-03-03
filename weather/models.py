from __future__ import unicode_literals
from django.db import models

class Country(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name

class Metric(models.Model):
	type = models.CharField(max_length=30)

	def __str__(self):
		return self.type	

	
class WeatherReport(models.Model):
	country = models.ForeignKey(Country, on_delete=models.CASCADE)
	metric_type = models.ForeignKey(Metric, on_delete=models.CASCADE)
	year = models.IntegerField()
	month = models.IntegerField()
	value = models.DecimalField(max_digits=10,decimal_places=3)
	class Meta:
		unique_together = (("country", "metric_type", "year", "month"),)

		def __str__(self):
			return self.country + self.year

