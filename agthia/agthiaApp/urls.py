from django.conf.urls.static import static # type: ignore
from django.urls import path # type: ignore
from django.conf import settings # type: ignore
from agthiaApp import views
from .views import image_list



urlpatterns = [
path("",views.home),
path("home",views.home,name="home"),
path("contacts/",views.contacts),
path('restaurant/<int:local_id>/', views.rest, name='rest'),
path('restaurant2/<int:inter_id>/', views.rest2, name='rest2'),
path("brand/",views.brand),
path('reserve/', views.reservation_view, name='reservation'),
path('mailus', views.mailus, name='mailus'),
path('admin_home/', views.admin_home, name='admin_home'),
path('local/',views.local),
path('upload/', views.upload_image, name='upload_image'),
path('inter/',views.inter),
path('upload1/', views.upload_image1, name='upload_image1'),
path('register_admin/', views.register_admin, name='register_admin'),
path('admin_reg/', views.admin_reg, name='admin_reg'),
path('login/', views.login, name='login'),
path('checklogin/', views.checklogin, name='checklogin'),
path('image_list/', views.image_list, name='image-list'),
path('add_restaurant/', views.add_restaurant, name='add_restaurant'),
path('add_restaurant2/', views.add_restaurant2, name='add_restaurant2'),
path('add_rest/', views.add_rest, name='add_rest'),
path('add_rest2/', views.add_rest2, name='add_rest2'),
path('add_profile/', views.add_profile, name='add_profile'),
path('profile/', views.profile_view, name='profile-view'),
path('edit_profile/<int:profile_id>/', views.edit_profile_view, name='edit-profile'),
path('save_profile/<int:profile_id>/', views.save_profile_view, name='save-profile'),
path('subscribe/', views.subscribe, name='subscribe'),

   



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)