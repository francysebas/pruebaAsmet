from rest_framework import routers
from .viewsets import PersonaViewSet, CasoViewSet, TipoPerViewSet, TipoDocViewSet, JuzgadoViewSet

router = routers.SimpleRouter()

router.register('persona', PersonaViewSet)
router.register('caso', CasoViewSet)
router.register('tipo', TipoPerViewSet)
router.register('juzgado', JuzgadoViewSet)
router.register('tipoDocumento', TipoDocViewSet)

urlpatterns = router.urls