from django.urls import path
from .views import index, thankYou
urlpatterns  = [
    path('', index, name='index' ),
    path('thank-you/', thankYou, name='thank-you' )
]