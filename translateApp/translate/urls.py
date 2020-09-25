from rest_framework import routers
from .api import TranslateViewSet

router = routers.DefaultRouter()
router.register('api/translate', TranslateViewSet, 'translate')
# router.register('translations', TranslateViewSet, 'getTexts')

urlpatterns = router.urls
