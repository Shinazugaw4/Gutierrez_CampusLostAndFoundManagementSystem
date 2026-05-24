from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('api/items/report', views.report_item),
    path('api/items', views.view_items),
    path('api/items/claim', views.claim_item),
]