from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import (Clients, Employees, Materials, Orders, OrderItems,
                     Orderstatuses, Producer, Products, Recipes, Roles,
                     Shifts, Statuses, Supplies, SupplyItems, SupplyStatuses)
from .serializers import (ClientSerializer, EmployeeSerializer, MaterialSerializer,
                           OrderSerializer, OrderItemSerializer, OrderStatusSerializer,
                           ProducerSerializer, ProductSerializer, RecipeSerializer,
                           RoleSerializer, ShiftSerializer, StatusSerializer,
                           SupplySerializer, SupplyItemSerializer, SupplyStatusSerializer)


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        name = self.request.query_params.get('name')
        if name:
            qs = qs.filter(client_name__icontains=name)
        return qs


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeeSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        lastname = self.request.query_params.get('lastname')
        role = self.request.query_params.get('role')
        if lastname:
            qs = qs.filter(lastname__icontains=lastname)
        if role:
            qs = qs.filter(id_role=role)
        return qs


class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Materials.objects.all()
    serializer_class = MaterialSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        name = self.request.query_params.get('name')
        producer = self.request.query_params.get('producer')
        if name:
            qs = qs.filter(material_name__icontains=name)
        if producer:
            qs = qs.filter(id_producer=producer)
        return qs


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        client = self.request.query_params.get('client')
        status_id = self.request.query_params.get('status')
        if client:
            qs = qs.filter(id_client=client)
        if status_id:
            qs = qs.filter(id_orderstatus=status_id)
        return qs


class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItems.objects.all()
    serializer_class = OrderItemSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        order = self.request.query_params.get('order')
        if order:
            qs = qs.filter(id_order=order)
        return qs


class OrderStatusViewSet(viewsets.ModelViewSet):
    queryset = Orderstatuses.objects.all()
    serializer_class = OrderStatusSerializer


class ProducerViewSet(viewsets.ModelViewSet):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        name = self.request.query_params.get('name')
        if name:
            qs = qs.filter(producer_name__icontains=name)
        return qs


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        name = self.request.query_params.get('name')
        if name:
            qs = qs.filter(product_name__icontains=name)
        return qs


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipes.objects.all()
    serializer_class = RecipeSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        product = self.request.query_params.get('product')
        if product:
            qs = qs.filter(id_product=product)
        return qs


class RoleViewSet(viewsets.ModelViewSet):
    queryset = Roles.objects.all()
    serializer_class = RoleSerializer


class ShiftViewSet(viewsets.ModelViewSet):
    queryset = Shifts.objects.all()
    serializer_class = ShiftSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        worker = self.request.query_params.get('worker')
        if worker:
            qs = qs.filter(id_worker=worker)
        return qs


class StatusViewSet(viewsets.ModelViewSet):
    queryset = Statuses.objects.all()
    serializer_class = StatusSerializer


class SupplyViewSet(viewsets.ModelViewSet):
    queryset = Supplies.objects.all()
    serializer_class = SupplySerializer

    def get_queryset(self):
        qs = super().get_queryset()
        supplier = self.request.query_params.get('supplier')
        if supplier:
            qs = qs.filter(id_supplier=supplier)
        return qs


class SupplyItemViewSet(viewsets.ModelViewSet):
    queryset = SupplyItems.objects.all()
    serializer_class = SupplyItemSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        supply = self.request.query_params.get('supply')
        if supply:
            qs = qs.filter(id_supply=supply)
        return qs


class SupplyStatusViewSet(viewsets.ModelViewSet):
    queryset = SupplyStatuses.objects.all()
    serializer_class = SupplyStatusSerializer
    
    