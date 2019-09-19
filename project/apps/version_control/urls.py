from django.conf.urls import url, include
from django.urls import path
# from rest_framework import routers
from rest_framework_nested import routers as nested_routers
from . import views

router = nested_routers.DefaultRouter()
router.register(r'clients', views.ClientsViewSet, base_name="clients")
router.register(r'repositories', views.RepositoriesViewSet, base_name="repositories")
router.register(r'environments', views.EnvironmentsViewSet, base_name="environments")
router.register(r'tags', views.TagsViewSet, base_name="tags")

urlpatterns = [
    url(r'^', include((router.urls, 'version_control'), namespace='version_control'))
]
