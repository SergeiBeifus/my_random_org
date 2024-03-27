from django.urls import path

from generate_password.views import index

urlpatterns = [
    path('', index, name='index', ),
]
