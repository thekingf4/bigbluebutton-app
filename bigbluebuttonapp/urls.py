from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import bigbluebuttonapp_view

urlpatterns = [
    url(r"^/$", bigbluebuttonapp_view , name="bigbluebuttonapp_view")
]

