
from django.urls import path
from apibasics import views
from .views import ArticleAPIView, ArticleDetails,GenericAPIView,GenericDetails

urlpatterns = [
    path('func_article/', views.article_list),
    path('func_detail/<int:pk>/', views.article_detail),
    
    path('class_article/',ArticleAPIView.as_view()),
    path('class_detail/<int:id>/', ArticleDetails.as_view()),
    
    path('generic_article/',GenericAPIView.as_view()),
    path('generic_detail/<int:pk>/',GenericDetails.as_view()),
]