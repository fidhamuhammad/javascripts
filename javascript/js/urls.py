from django.urls import path
from .import views

urlpatterns=[
     path('add',views.add),
     path('elements',views.elements),
     path('largest',views.largest),
     path('secondlargest',views.secondlargest),
     path('search',views.search)
]