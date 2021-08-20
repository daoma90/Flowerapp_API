from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('comment-list/<str:pk>', views.commentList, name="comment-list"),
    path('comment-create/', views.commentCreate, name="comment-create"),
    path('comment-update/<str:pk>/', views.commentUpdate, name="comment-update"),
    path('comment-delete/<str:pk>/', views.commentDelete, name="comment-delete")
]