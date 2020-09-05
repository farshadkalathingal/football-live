from django.urls import path
from scorecard import views

urlpatterns = [

    path('', views.Match_list, name='Match'),
    path('results/', views.Results_list, name='Result'),
    path('getSubcategory/', views.get_subcategoty, name='Sub-Category'),
]
