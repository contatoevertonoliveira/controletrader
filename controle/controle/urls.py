from django.contrib import admin
from django.urls import path
from app.views import home, form
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('form/', form, name="form")
]
