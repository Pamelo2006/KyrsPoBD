from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('brends/', views.brends, name='brends'),
    path('useracount/', views.useracount, name='useracount'),
    path('postuser/', views.post_user, name='postuser'),
    path('handleuseractions/', views.handle_user_actions, name='handleuseractions'),
    path('usercard/', views.user_card, name='usercard')
]