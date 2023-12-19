
from django.urls import path
from . import views
from.views import FilterView, HomeView

urlpatterns = [
    
    path('', HomeView.as_view(), name="home"),
    path('filterform/', FilterView, name="filter"),
    path('/category/<category>/', views.CategoryView.as_view(), name='category'),
 
    
    

    

]
