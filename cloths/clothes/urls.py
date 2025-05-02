from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage),
    path('mencollection',views.mencollection),
    path('shoes',views.shoes),
    path('womencollection',views.womencollection),
    path('watch',views.watch),
    path('accessoires',views.accessories),
    path('tshirt',views.tshirt)
]