
from django.urls import path
from profiles.api import views


url_patters = [
    path("user-profiles/",views.ProfileList.as_view(),name="profiles"),



]