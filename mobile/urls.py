from django.urls import path
from .views import CreateMobile, ListMobile

urlpatterns = [
    path('create/', CreateMobile.as_view(), name='create-mobile'),
    path('', ListMobile.as_view(), name='list-mobile'),
]
