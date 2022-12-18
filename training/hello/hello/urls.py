from django.contrib import admin
from django.urls import path

#Here we can see the different urls that are created to be able to go to the different views of the web.
urlpatterns = [
    path('admin/', admin.site.urls),
]

from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('polls/', include('polls.urls')),
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
]