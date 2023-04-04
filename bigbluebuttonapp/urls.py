from django.conf.urls import url
from django.urls import path, include, re_path
from django.contrib.auth.decorators import login_required

from .views import bigbluebuttonapp_view

# urlpatterns = [
#     url(r"^/$", bigbluebuttonapp_view , name="bigbluebuttonapp_view")
# ]


urlpatterns = [
    path(r"^/$", bigbluebuttonapp_view , name="bigbluebuttonapp_view")
]
