"""carsales URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib import admin
from handler import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home_view, name="home"),
    path("about/", views.about_view, name="about"),
    path("media/", views.media_view, name="media"),
    path("listed_items/", views.listed_item_view, name="listed_items"),
    path("contact/", views.contact_view, name="contact"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("register/", views.register_view, name="register"),
    path("search/", views.search_view, name="search"),
    path("dashboard/", views.dashboard_view, name="dashboard"),
    path("purchase/<int:id>/", views.purchase_view, name="purchase"),
    path("listed_item_purchase/<int:id>/", views.listed_item_purchase_view, name="listed_item_purchase"),
    path("custom_purchase/", views.custom_purchase_view, name="custom_purchase"),
    path("create_listing/", views.create_listing_view, name="create_listing"),
    path("listed_item/<int:id>/", views.listed_item_detail_view, name="listed_item_detail"),
    path("delete_listed_product/<int:id>/", views.listed_item_delete_view, name="delete_listed_product"),
    path("item/<int:id>/", views.item_detail_view, name="item_detail"),
    path("success/", views.success_view, name="success"),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
