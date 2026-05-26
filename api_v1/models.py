# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Clients(models.Model):
    id_client = models.AutoField(db_column='ID_client', primary_key=True)  # Field name made lowercase.
    client_name = models.CharField(db_column='Client_name', max_length=50, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    clientlogin = models.CharField(db_column='ClientLogin', max_length=20, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    clientpassword = models.CharField(db_column='ClientPassword', max_length=20, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clients'


class Employees(models.Model):
    id_employee = models.AutoField(db_column='ID_employee', primary_key=True)  # Field name made lowercase.
    firstname = models.CharField(db_column='FirstName', max_length=50, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    lastname = models.CharField(db_column='LastName', max_length=50, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    patronymic = models.CharField(db_column='Patronymic', max_length=50, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.
    employeelogin = models.CharField(db_column='EmployeeLogin', max_length=20, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    employeepassword = models.CharField(db_column='EmployeePassword', max_length=20, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    id_role = models.ForeignKey('Roles', models.DO_NOTHING, db_column='ID_role')  # Field name made lowercase.
    id_status = models.ForeignKey('Statuses', models.DO_NOTHING, db_column='ID_status')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'employees'


class InventoryLogs(models.Model):
    id_log = models.AutoField(db_column='ID_log', primary_key=True)  # Field name made lowercase.
    logtime = models.DateTimeField(db_column='LogTime')  # Field name made lowercase.
    id_material = models.ForeignKey('Materials', models.DO_NOTHING, db_column='ID_material')  # Field name made lowercase.
    change_type = models.CharField(db_column='Change_type', max_length=50, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    quantity = models.DecimalField(db_column='Quantity', max_digits=10, decimal_places=2)  # Field name made lowercase.
    id_supply = models.ForeignKey('Supplies', models.DO_NOTHING, db_column='ID_supply', blank=True, null=True)  # Field name made lowercase.
    id_order = models.ForeignKey('Orders', models.DO_NOTHING, db_column='ID_order', blank=True, null=True)  # Field name made lowercase.
    comment = models.CharField(db_column='Comment', max_length=255, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'inventory_logs'


class Materials(models.Model):
    id_material = models.AutoField(db_column='ID_material', primary_key=True)  # Field name made lowercase.
    material_name = models.CharField(db_column='Material_name', max_length=100, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=2)  # Field name made lowercase.
    countonwarehouse = models.DecimalField(db_column='CountOnWarehouse', max_digits=10, decimal_places=2)  # Field name made lowercase.
    id_producer = models.ForeignKey('Producer', models.DO_NOTHING, db_column='ID_producer')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'materials'


class Orderstatuses(models.Model):
    id_orderstatus = models.AutoField(db_column='ID_orderStatus', primary_key=True)  # Field name made lowercase.
    statusdescription = models.CharField(db_column='StatusDescription', max_length=50, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orderStatuses'


class OrderItems(models.Model):
    pk = models.CompositePrimaryKey('id_order', 'id_product')
    id_order = models.ForeignKey('Orders', models.DO_NOTHING, db_column='ID_order')
    id_product = models.ForeignKey('Products', models.DO_NOTHING, db_column='ID_product')
    product_count = models.IntegerField(db_column='Product_count')
    sale_price = models.DecimalField(db_column='Sale_price', max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'order_items'


class Orders(models.Model):
    id_order = models.AutoField(db_column='ID_order', primary_key=True)  # Field name made lowercase.
    ordertime = models.DateTimeField(db_column='OrderTime')  # Field name made lowercase.
    id_client = models.ForeignKey(Clients, models.DO_NOTHING, db_column='ID_client')  # Field name made lowercase.
    id_orderstatus = models.ForeignKey(Orderstatuses, models.DO_NOTHING, db_column='ID_orderStatus')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orders'


class Producer(models.Model):
    id_producer = models.AutoField(db_column='ID_producer', primary_key=True)  # Field name made lowercase.
    producer_name = models.CharField(db_column='Producer_name', max_length=50, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    prodlogin = models.CharField(db_column='ProdLogin', max_length=20, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    prodpassword = models.CharField(db_column='ProdPassword', max_length=20, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'producer'


class Products(models.Model):
    id_product = models.AutoField(db_column='ID_product', primary_key=True)  # Field name made lowercase.
    product_name = models.CharField(db_column='Product_name', max_length=50, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.
    price = models.DecimalField(db_column='Price', max_digits=10, decimal_places=2)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'products'


class Recipes(models.Model):
    pk = models.CompositePrimaryKey('id_product', 'id_material')
    id_product = models.ForeignKey(Products, models.DO_NOTHING, db_column='ID_product')
    id_material = models.ForeignKey(Materials, models.DO_NOTHING, db_column='ID_material')
    material_count = models.DecimalField(db_column='Material_count', max_digits=10, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'recipes'


class Roles(models.Model):
    id_role = models.AutoField(db_column='ID_role', primary_key=True)  # Field name made lowercase.
    roledescription = models.CharField(db_column='RoleDescription', max_length=50, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'roles'


class Shifts(models.Model):
    pk = models.CompositePrimaryKey('id_shift', 'id_worker')
    id_shift = models.IntegerField(db_column='ID_shift')
    shift_name = models.CharField(max_length=100, db_collation='Cyrillic_General_CI_AS', blank=True, null=True)
    shifttime = models.DateTimeField(db_column='ShiftTime', blank=True, null=True)
    id_admin = models.ForeignKey(Employees, models.DO_NOTHING, db_column='ID_admin', blank=True, null=True)
    id_worker = models.ForeignKey(Employees, models.DO_NOTHING, db_column='ID_worker', related_name='shifts_id_worker_set')

    class Meta:
        managed = False
        db_table = 'shifts'


class Statuses(models.Model):
    id_status = models.AutoField(db_column='ID_status', primary_key=True)  # Field name made lowercase.
    statusdescription = models.CharField(db_column='StatusDescription', max_length=50, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'statuses'


class Supplies(models.Model):
    id_supply = models.AutoField(db_column='ID_supply', primary_key=True)  # Field name made lowercase.
    supplytime = models.DateTimeField(db_column='SupplyTime')  # Field name made lowercase.
    id_supplier = models.ForeignKey(Producer, models.DO_NOTHING, db_column='ID_supplier')  # Field name made lowercase.
    id_supply_status = models.ForeignKey('SupplyStatuses', models.DO_NOTHING, db_column='ID_supply_status', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'supplies'


class SupplyItems(models.Model):
    pk = models.CompositePrimaryKey('id_supply', 'id_material')
    id_supply = models.ForeignKey(Supplies, models.DO_NOTHING, db_column='ID_supply')
    id_material = models.ForeignKey(Materials, models.DO_NOTHING, db_column='ID_material')
    material_count = models.IntegerField(db_column='Material_count')
    cost_price = models.DecimalField(db_column='Cost_price', max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'supply_items'


class SupplyStatuses(models.Model):
    id_status = models.AutoField(db_column='ID_status', primary_key=True)  # Field name made lowercase.
    statusname = models.CharField(db_column='StatusName', max_length=50, db_collation='Cyrillic_General_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'supply_statuses'


class Sysdiagrams(models.Model):
    name = models.CharField(max_length=128, db_collation='Cyrillic_General_CI_AS')
    principal_id = models.IntegerField()
    diagram_id = models.AutoField(primary_key=True)
    version = models.IntegerField(blank=True, null=True)
    definition = models.BinaryField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sysdiagrams'
        unique_together = (('principal_id', 'name'),)
