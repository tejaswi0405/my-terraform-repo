from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Product.urls')),  # Home page and product-related URLs
    path('accounts/', include('django.contrib.auth.urls')),  # Built-in auth URLs
    path('accounts/', include('accounts.urls')),  # Your custom authentication URLs

    # Fix the logout path

]

# Static and media file handling
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
