from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic.base import RedirectView
from social.views import ProfileUpdateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('social/', include('social.urls')),
    path('accounts/', include('registration.backends.default.urls')),
    path('profile/edit/<int:pk>',ProfileUpdateView.as_view()),
    path('',RedirectView.as_view(url='social/')),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
