from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from .import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^submit_project/', views.submit_project, name='submit_project'),
    url(r'^create_tag/', views.create_tag, name='create_tag'),
    url(r'^create_project_tag/', views.create_project_tag, name='create_project_tag'),
    url(r'^project/(\d+)',views.project,name='project'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
