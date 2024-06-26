from rest_framework import routers
from .views import PostViewSet, PatientGetViewSet


router = routers.DefaultRouter()
router.register('postpatient', PostViewSet, 'Patient'),
router.register('getpatient', PatientGetViewSet, 'patient_get')


urlpatterns = router.urls
