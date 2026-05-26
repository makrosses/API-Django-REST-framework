"""
URL configuration for library_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

from api_v1.views import (ClientViewSet, EmployeeViewSet, MaterialViewSet,
                           OrderViewSet, OrderItemViewSet, OrderStatusViewSet,
                           ProducerViewSet, ProductViewSet, RecipeViewSet,
                           RoleViewSet, ShiftViewSet, StatusViewSet,
                           SupplyViewSet, SupplyItemViewSet, SupplyStatusViewSet)

router = DefaultRouter()
router.register(r'clients', ClientViewSet)
router.register(r'employees', EmployeeViewSet)
router.register(r'materials', MaterialViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'order-items', OrderItemViewSet)
router.register(r'order-statuses', OrderStatusViewSet)
router.register(r'producers', ProducerViewSet)
router.register(r'products', ProductViewSet)
router.register(r'recipes', RecipeViewSet)
router.register(r'roles', RoleViewSet)
router.register(r'shifts', ShiftViewSet)
router.register(r'statuses', StatusViewSet)
router.register(r'supplies', SupplyViewSet)
router.register(r'supply-items', SupplyItemViewSet)
router.register(r'supply-statuses', SupplyStatusViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]

