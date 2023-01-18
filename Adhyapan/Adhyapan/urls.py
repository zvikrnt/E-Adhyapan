from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from Adhyapan import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.default.urls')),                 

    path('learn/', include('learn.urls')), 
    path('', RedirectView.as_view(url="learn/")),    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
