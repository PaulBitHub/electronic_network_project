from rest_framework import serializers
from models import NetworkNode, Supplier, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
        read_only_fields = ('debt_to_supplier',)  # запрет обновления поля через API

class NetworkNodeSerializer(serializers.ModelSerializer):
    supplier = SupplierSerializer(read_only=True)
    supplier_id = serializers.PrimaryKeyRelatedField(
        queryset=Supplier.objects.all(),
        write_only=True,
        source='supplier'
    )
    products = ProductSerializer(many=True, read_only=True)
    product_ids = serializers.PrimaryKeyRelatedField(
        queryset=Product.objects.all(),
        write_only=True,
        many=True,
        source='products'
    )
    class Meta:
        model = NetworkNode
        fields = '__all__'

    def validate(self, data):
        parent = data.get('parent')
        level = data.get('level')

        if parent and level is not None:
            if level <= parent.level:
                raise serializers.ValidationError("Уровень узла должен быть выше, чем у родительского")
        return data
