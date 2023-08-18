# Create web/urls.py and paste the following
from django.urls import path
from . import views
from django.views.generic import TemplateView
app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("protfolio_nayel", views.protfolio_nayel, name="protfolio_nayel"),
]





