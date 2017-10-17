
from django.conf.urls import url
from . import views

urlpatterns = [
    # defines Music app homepage
    url(r"^$", views.index, name="index")
]
