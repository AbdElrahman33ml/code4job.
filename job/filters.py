import django_filters
from .models import job

class JobFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    experience__gt = django_filters.NumberFilter(field_name='experience', lookup_expr='gt')
    experience__lt = django_filters.NumberFilter(field_name='experience', lookup_expr='lt')


    class Meta:
        model = job
        fields = '__all__'
        exclude = ['id','slug','owner','image','vacancy','salary',]