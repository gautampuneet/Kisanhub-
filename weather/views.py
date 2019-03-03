import dateutil.parser
from weather.serializers import GetWetherReportSerializer
from .models import WeatherReport,Country,Metric
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from rest_framework import views
from rest_framework.generics import ListAPIView

class GetWetherReport(ListAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = GetWetherReportSerializer
    model = WeatherReport
    def get_queryset(self):
        start_date = self.request.query_params.get("start_date")
        end_date = self.request.query_params.get("end_date")
        metric_type = self.request.query_params.get("metric_type")
        location = self.request.query_params.get("location")
        queryset = self.model.objects.none()
        if start_date and end_date and metric_type and location:
            start_date = dateutil.parser.parse(start_date)
            end_date = dateutil.parser.parse(end_date)
            queryset = self.model.objects.filter(
                year__gte=start_date.year,
                year__lte=end_date.year,
                month__gte=start_date.month,
                metric_type__type=metric_type,
                country__name=location
            )
        return queryset

        
