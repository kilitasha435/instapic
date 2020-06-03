from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('',views.timeline,name='timeline'),
    path('search/', views.search_results, name = 'search_results'),
    path('explore/', views.explore, name = 'explore'),
    path('accounts/profile/(\d+)', views.profile, name = 'profile'),
    path('new/post/', views.new_post, name = 'new-post'),
    path('accounts/edit-profile/',views.edit_profile, name = 'edit-profile'),


]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)