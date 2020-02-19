from django.urls import path

from . import views

urlpatterns =[
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing1, name='listing1'),
    path('search', views.search, name='search'),
]