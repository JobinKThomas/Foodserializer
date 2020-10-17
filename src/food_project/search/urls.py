from django.conf.urls import url

from . import views

urlpatterns = [
    url('foods/', views.FoodAPIView.as_view()),
]
