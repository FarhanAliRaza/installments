from django.contrib import admin
from django.urls import path
from customer.views import home, pages, create_user, create_item, detail_item, update_month, invoice, invoices, customer_delete
from django.urls import path, include, re_path # new
from django.conf.urls.static import static

try:
    from inst import local_settings as settings
except:
    from inst import  settings as settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')), # new

    path('', home),
    path('customer_delete/<str:id>/', customer_delete),

    path('create-user/', create_user),
    path('invoices/', invoices),

    path('invoice/<str:id>/', invoice),

    path('create-item/', create_item),
    path('item/<str:id>/', detail_item),
    path('item/<str:item_id>/<str:id>/', update_month),




    re_path(r'^.*\.*', pages, name='pages'),



]

# if settings.DEPLOYED:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# else:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

    

