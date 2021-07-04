from ecommerce.views import *
from rest_framework.routers import DefaultRouter

app_name = "ecommerce"
router = DefaultRouter()
router.register("categories", CategoryViewSet, basename="categories")
router.register("products", ProductViewSet, basename="products")
router.register("suppliers", SupplierViewSet, basename="suppliers")
router.register("carts", CartViewSet, basename="carts")
router.register("cartitems", CartItemViewSet, basename="cartitems")
router.register("stockups", StockUpViewSet, basename="stockups")

urlpatterns = router.urls
