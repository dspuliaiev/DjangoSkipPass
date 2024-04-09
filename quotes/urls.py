from django.urls import path
from .import views

app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='root'),
    path('<int:page>/', views.main, name='root-paginate'),
    path('add-quote/', views.add_quote, name='add-quote'),
    path('add-author/', views.add_author, name='add-author'),

]
