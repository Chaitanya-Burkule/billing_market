from sales_app.models import Invoice , InvoiceProduct
from rest_framework import serializers


class InvoiceProductSerializer(serializers.ModelSerializer):

    invoice_product_id = serializers.IntegerField(read_only=True)
    invoice = serializers.SerializerMethodField()
    product_invoice = serializers.SerializerMethodField()

    class Meta:
        model = InvoiceProduct
        fields = '__all__'

    def get_invoice(self, obj):
        return f'{obj.invoice.invoice_number}'
    
    def get_product_invoice(self, obj):
        return f'{obj.product_invoice.product_name}'
    
    
class InvoiceSerializers(serializers.ModelSerializer):
    
    invoice_date = serializers.DateField(read_only=True)
    product_in_invoice = InvoiceProductSerializer(read_only=True, many=True)
    customer = serializers.SerializerMethodField()
    invoice_created_by  = serializers.SerializerMethodField()

    class Meta:
        model = Invoice
        fields = "__all__"

    def get_customer(self, obj):
        return f'{obj.customer.name}'
    
    def get_invoice_created_by(self, obj):
        return f'{obj.invoice_created_by.first_name} {obj.invoice_created_by.last_name}'