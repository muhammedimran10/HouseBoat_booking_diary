from django.urls import path
from booking import views

urlpatterns = [
    path('',views.myboats,name='myboats'),
    path('addboat/',views.addboat,name='addboat'),
    path('addowners/<int:id>',views.addowners,name='addowners'),
    path('addowner/<int:id>/<int:b_id>/',views.addowner,name='addowner'),

]
