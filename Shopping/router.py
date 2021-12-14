from rest_framework import routers
from Order.viewsets import OrderViewset

router = routers.DefaultRouter()
router.register(r'Order',OrderViewset)