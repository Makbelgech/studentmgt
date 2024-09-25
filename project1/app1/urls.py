from django.urls import path
from . import views
urlpatterns = [
    path('home/', views.home, name='home'),
    # path('app1/',views.index,name = 'index'),
]
