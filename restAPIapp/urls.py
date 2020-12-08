from django.urls import path
from . import views
urlpatterns = [
    # path('article/', views.articleList, name = 'api'),
    # path('detail/<int:pk>/', views.articleDetail, name = 'articleDetail'),
    path('article/', views.articleAPIview.as_view(), name = 'articleAPIview'),
    path('detail/<int:pk>/', views.articleDetails.as_view(), name = 'articleDetails'),

]
