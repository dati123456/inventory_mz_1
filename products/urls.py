from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import ItemViewSet, CategoryViewSet


router = SimpleRouter()
router.register(r'items', ItemViewSet)
router.register(r'category', CategoryViewSet)
urlpatterns = router.urls