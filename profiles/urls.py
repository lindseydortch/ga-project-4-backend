from rest_framework import routers
from .api import ProfilesViewSet

router = routers.DefaultRouter()
router.register('profiles', ProfilesViewSet, 'profiles')

urlpatterns = router.urls