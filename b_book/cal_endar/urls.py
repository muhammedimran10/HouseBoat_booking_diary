from django.urls import path
from cal_endar import views

urlpatterns = [
    path('',views.home,name='home'),
    path('date_select/<int:d>/<int:m>/<int:y>/<int:b_id>',views.home,name="date_select"),

    path('p_month/',views.p_month,name="p_month"),
    path('n_month/',views.n_month,name="n_month"),

]