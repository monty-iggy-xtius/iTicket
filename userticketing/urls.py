from django.urls import path
from . import views

# views for the userticketing app
urlpatterns = [
	path('', views.index_route, name="index"),
	path('dashboard/', views.dashboard_route, name="dashboard"),
	path('about/', views.about_route, name="about"),
	path('blog/', views.blog_route, name="blog"),
	path('contact/', views.contact_route, name="contact"),
]