from django.urls import path
from .views import home_view, about_us


urlpatterns = [
    path("", home_view),
    path("about/", about_us),
]
