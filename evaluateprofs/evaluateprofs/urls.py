"""evaluateprofs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, re_path
from professors.views import (professors_list, professor_profile, home_page,
                              professors_search, about_page, terms_page)
from accounts.views import activate, login_view, logout_view, register_view


urlpatterns = [
    path('', home_page),
    path('about/', about_page),
    path('admin/', admin.site.urls),
    path('login/', login_view),
    path('logout/', logout_view),
    path('professors/', professors_list),
    path('professors/<int:id>/', professor_profile),
    path('register/', register_view),
    path('search/', professors_search),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            activate, name='activate'),
    path('terms/', terms_page),
    re_path(r'^password_reset/$', auth_views.PasswordResetView.as_view(),
            name='password_reset'),
    re_path(r'^password_reset/done/$',
            auth_views.PasswordResetDoneView.as_view(),
            name='password_reset_done'),
    re_path(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            auth_views.PasswordResetConfirmView.as_view(),
            name='password_reset_confirm'),
    re_path(r'^reset/done/$', auth_views.PasswordResetCompleteView.as_view(),
            name='password_reset_complete'),
]
