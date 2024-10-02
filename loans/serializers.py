from rest_framework import serializers
from loans.models import Loan

class LoanSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'

class EligibilityFormSerializer(serializers.Serializer):
    mortgagable_property = serializers.CharField(max_length=20)
    property_valuation = serializers.IntegerField()
    taxable_monthly_income = serializers.IntegerField()
    