import os
import requests
from django.core.management.base import BaseCommand
from weather.models import WeatherReport, Country, Metric
class Command(BaseCommand):
    help = 'Fetch JSON files for all the locations and metrices' 

    def handle(self,*args,**kwargs):
        files = os.listdir("data")
        for file in files:
            print(file.split("_")[0], file.split("_")[1])
            country = Country.objects.get(name=file.split("_")[0])
            metric_type = Metric.objects.get(type=file.split("_")[1].split(".")[0])
            with open("./data/" + file) as f:
                final_list = []
                for i, lines in enumerate(f):
                    lines = lines.strip().split(" ")
                    lines = filter(None, lines)
                    if i > 0:
                        for item in enumerate(lines):
                            if item > 0:
                                try:
                                    WeatherReport.objects.create(
                                        year=lines[0],
                                        month=1,
                                        value=lines[1] if len(lines) > 1 else 0,
                                        country=country,
                                        metric_type=metric_type,
                                    )
                                except:
                                    pass
                                try:
                                    WeatherReport.objects.create(
                                        year=lines[0],
                                        month=2,
                                        value=lines[2] if len(lines) > 2 else 0,
                                        country=country,
                                        metric_type=metric_type,
                                    )
                                except:
                                    pass
                                try:
                                    WeatherReport.objects.create(
                                        year=lines[0],
                                        month=3,
                                        value=lines[3] if len(lines) > 3 else 0,
                                        country=country,
                                        metric_type=metric_type,
                                    )
                                except:
                                    pass
                                try:
                                    WeatherReport.objects.create(
                                        year=lines[0],
                                        month=4,
                                        value=lines[4] if len(lines) > 4 else 0,
                                        country=country,
                                        metric_type=metric_type,
                                    )
                                except:
                                    pass
                                try:
                                    WeatherReport.objects.create(
                                        year=lines[0],
                                        month=5,
                                        value=lines[5] if len(lines) > 5 else 0,
                                        country=country,
                                        metric_type=metric_type,
                                    )
                                except:
                                    pass
                                try:
                                    WeatherReport.objects.create(
                                        year=lines[0],
                                        month=6,
                                        value=lines[6] if len(lines) > 6 else 0,
                                        country=country,
                                        metric_type=metric_type,
                                    )
                                except:
                                    pass
                                try:
                                    WeatherReport.objects.create(
                                        year=lines[0],
                                        month=7,
                                        value=lines[7] if len(lines) > 7 else 0,
                                        country=country,
                                        metric_type=metric_type,
                                    )
                                except:
                                    pass
                                try:
                                    WeatherReport.objects.create(
                                        year=lines[0],
                                        month=8,
                                        value=lines[8] if len(lines) > 8 else 0,
                                        country=country,
                                        metric_type=metric_type,
                                    )
                                except:
                                    pass
                                try:
                                    WeatherReport.objects.create(
                                        year=lines[0],
                                        month=9,
                                        value=lines[9] if len(lines) > 9 else 0,
                                        country=country,
                                        metric_type=metric_type,
                                    )
                                except:
                                    pass
                                try:
                                    WeatherReport.objects.create(
                                        year=lines[0],
                                        month=10,
                                        value=lines[10] if len(lines) > 10 else 0,
                                        country=country,
                                        metric_type=metric_type,
                                    )
                                except:
                                    pass
                                try:
                                    WeatherReport.objects.create(
                                        year=lines[0],
                                        month=11,
                                        value=lines[11] if len(lines) > 11 else 0,
                                        country=country,
                                        metric_type=metric_type,
                                    )
                                except:
                                    pass
                                try:
                                    WeatherReport.objects.create(
                                        year=lines[0],
                                        month=12,
                                        value=lines[12] if len(lines) > 12 else 0,
                                        country=country,
                                        metric_type=metric_type,
                                    )
                                except:
                                    pass
