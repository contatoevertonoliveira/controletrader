from django.contrib import admin
from django.urls import path
from app.views import home, form, create, view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('form/', form, name="form"),
    path('create/', create, name="create"),
    path('view/', view, name="view")
]
