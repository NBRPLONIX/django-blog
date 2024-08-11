from django.urls import path
from . import views

# http://137.0.0.1:8000/category/4
urlpatterns = [
    path('<int:category_id>/', views.posts_by_category, name='posts_by_category')
    
]