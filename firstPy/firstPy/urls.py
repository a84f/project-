from django.urls import path, include
from django.contrib import admin

admin.site.title="Gims Login"
admin.site.site_header="Gims Admin pandel"
admin.site.index_title="Gims"
urlpatterns = [
    path('',include('myApp.urls')),
    path('admin/', admin.site.urls),
]
