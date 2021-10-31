"""inst URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from customer.views import home, pages, create_user, create_item, detail_item, update_month, invoice, invoices
from django.urls import path, include, re_path # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # new

    path('', home),
    path('create-user/', create_user),
    path('invoices/', invoices),

    path('invoice/<str:id>/', invoice),

    path('create-item/', create_item),
    path('item/<str:id>/', detail_item),
    path('item/<str:item_id>/<str:id>/', update_month),




    re_path(r'^.*\.*', pages, name='pages'),



]
