import django_filters
from .models import Mobile


class MobileFilter(django_filters.FilterSet):
    brand_name = django_filters.CharFilter(lookup_expr='icontains', label='نام برند')
    
    class Meta:
        model = Mobile
        fields = {
            'brand_nationality': ['exact'],
            'made_in': ['exact'],
        }
