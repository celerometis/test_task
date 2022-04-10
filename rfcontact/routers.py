from rest_framework.routers import DefaultRouter

from contacts.viewsets import ContactViewSet

router = DefaultRouter()
router.register('contact-route',ContactViewSet, basename='contacts')

urlpatterns = router.urls