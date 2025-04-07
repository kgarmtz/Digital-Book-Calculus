"""Book URL Configuration
"""
from django.conf import settings
from django.contrib import admin, sitemaps
from django.conf.urls.static import static
from django.urls import path, include, re_path
# Import for Google AddSense
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView
# SEO stuff
from django.contrib.sitemaps.views import sitemap
from applications.home.sitemap import (
    SectionSitemap,
    Sitemap
)

# Our main urls
urlpatterns_main = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('polilibroescom/', admin.site.urls),
    path('recurso-digital/', include('applications.book.urls')),
    path('', include('applications.home.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path(
        "ads.txt",
        RedirectView.as_view(url=staticfiles_storage.url("ads.txt")),
    ),
]

urlpatterns_main += static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Create the Sitemap object that generates the XML file
sitemaps = {
    # The url structure is based on the main page of the site 'main.html' -- main url
    'site': Sitemap(
        [
            'home_app:index'
        ]
    ),

    # Subsequents url
    'secciones': SectionSitemap
}

urlpatterns_sitemap = [
    path(
        'sitemap.xml', 
        sitemap, 
        {'sitemaps': sitemaps},
        name = 'django.contrib.sitemaps.views.sitemap'
    ),
]


urlpatterns = urlpatterns_main + urlpatterns_sitemap