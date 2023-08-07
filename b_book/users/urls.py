from django.urls import path
from users import views
urlpatterns = [

    path('',views.home,),
    path('signup/',views.signup,name='signup'),
]
