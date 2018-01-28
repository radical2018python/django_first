from django.conf.urls import url
from firstapp import views

urlpatterns = [

    url(r'^view/',views.myView),
    url(r'^view1/',views.myView1),
    url(r'^view2/',views.myView2),
    url(r'^view3/',views.myView3),
    url(r'^\w',views.myView),

]