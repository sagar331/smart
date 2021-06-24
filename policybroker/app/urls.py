from rest_framework.routers import DefaultRouter
from app import views
router = DefaultRouter()
router.register('quotation',views.QuotationViewSet,basename='Quotation')
router.register('quo2',views.Quotation2ViewSet,basename='Quo2')
router.register('Quotations2',views.Quotation2ViewSet,basename='Quotations2')
router.register('veh',views.VehicleViewSet,basename='ve')
urlpatterns = router.urls