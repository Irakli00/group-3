from django.urls import path
from .views import (car_landing_page, CarListView, CarCreateView, CarDetailView, CarUpdateView, CarDeleteView,
                    CarSearchView)
# car_landing_page CarLandingPage

urlpatterns=[
    path('car/',car_landing_page,name="car_landing"),
    path('car/list',CarListView.as_view(),name="car_list"),
    path('car/new',CarCreateView.as_view(),name="car_new"),
    path('car/<int:pk>',CarDetailView.as_view(),name="car_detail"),
    path('car/<int:pk>/update',CarUpdateView.as_view(),name="car_update"),
    path('car/<int:pk>/delete',CarDeleteView.as_view(),name="car_delete"),
    path('car/search',CarSearchView.as_view(),name="car_delete"),
]