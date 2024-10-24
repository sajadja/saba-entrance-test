from django.views.generic.edit import CreateView
from django_filters.views import FilterView
from .filters import MobileFilter
from .models import Mobile
from django.urls import reverse_lazy


class CreateMobile(CreateView):
    model = Mobile
    fields = '__all__'
    success_url = reverse_lazy('list-mobile')


class ListMobile(FilterView):
    model = Mobile
    filterset_class = MobileFilter
