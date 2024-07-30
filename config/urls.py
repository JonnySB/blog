from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, path

from mysite.blog.sitemaps import PostSitemap

sitemaps = {
    'posts': PostSitemap,
}

urlpatterns = [
    path("admin/", admin.site.urls),
    path("blog/", include("mysite.blog.urls", namespace="blog")),
    path(
        "sitemap.xml",
        sitemap,
        {'sitemaps': sitemaps},
        name='django.contrib.sitemaps.views.sitemap',
    ),
]
