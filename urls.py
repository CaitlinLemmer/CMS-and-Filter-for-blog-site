#from members.urls import path
from django.urls import path
from . import views
from.views import FilterView, AusTripsView, HikingSaView, SaTripsView, ArticleDetailView, UpdatePostView, DeletePostView, AddPostView, AddCategoryView, CategoryListView, CategoryView, HomeView
#from django.contrib.auth import views as auth_views
#from members import views

urlpatterns = [
    
    path('', HomeView.as_view(), name="home"),
    path('filterform/', FilterView, name="filter"),
    
    #path('', views.home, name='home'),
    path('austrips/', AusTripsView.as_view(), name='austrips-page'),
    path('contact/', views.contact, name='contact-page'),
    path('hikingsa/', HikingSaView.as_view(), name='hikingsa-page'),
    path('satrips/', SaTripsView.as_view(), name='satrips-page'),
    path('started/', views.started, name='started-page'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article-detail'),
    path('add_post/', AddPostView.as_view(), name="add_post"),
    path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/remove', DeletePostView.as_view(), name='delete_post'),
    path('add_category/', AddCategoryView.as_view(), name="add_category"),
    
    path('category-list/', CategoryListView, name='category-list'),
    #path('post_list', HomePostListView, name='post_list'),
    #path('category/<str:cats>/', CategoryView, name='category'),
    path('/category/<category>/', views.CategoryView.as_view(), name='category'),
 
    
    

    

]
