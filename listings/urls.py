from django.urls import path

from . import views
# first path ' ' -> /listing
#second path represents /listing/id -> it's represented as <int:listing_id>
# 3rd path - > corresponds to /listing/search
urlpatterns = [
    path('', views.index, name='listings'),
    path('<int:listing_id>', views.listing, name='listing'),
    path('search', views.search, name='search'),
] 
