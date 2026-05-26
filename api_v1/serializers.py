from rest_framework import serializers
from .models import (Clients, Employees, Materials, Orders, OrderItems,
                     Orderstatuses, Producer, Products, Recipes, Roles,
                     Shifts, Statuses, Supplies, SupplyItems, SupplyStatuses)


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clients
        fields = '__all__'


class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statuses
        fields = '__all__'


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = '__all__'


class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = '__all__'


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Materials
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'


class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orderstatuses
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItems
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipes
        fields = '__all__'


class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shifts
        fields = '__all__'


class SupplyStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplyStatuses
        fields = '__all__'


class SupplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplies
        fields = '__all__'


class SupplyItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplyItems
        fields = '__all__'