from django.urls import path
#create a mapping between the path and the view
from .views import login_view, reg_view, logout_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('register/', reg_view.as_view(), name='register'),
    path('logout/', logout_view, name='logout'),

]
