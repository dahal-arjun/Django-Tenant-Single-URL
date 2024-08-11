from django.contrib import admin
from django.urls import include, re_path, path

urlpatterns = [
    path("api/admin/", admin.site.urls),
    path("api/sweet/", include("sweet_tenant.urls")),
    path("api/auth/", include("login.urls")),

]
