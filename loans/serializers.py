from rest_framework import serializers
from loans.models import Loans

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loans
        fields = '__all__'


class EligibilityFormSerializer(serializers.Serializer):
    real_estate = serializers.ChoiceField(choices=['Land', 'Apartment', 'Commercial', 'Residence'],  
        allow_blank=True)
    other_mortgageables = serializers.MultipleChoiceField(choices=['Automobile', 'Machinery/Equipment',
        'Furniture'], allow_blank=True)
    property_valuation = serializers.IntegerField()
    taxable_annual_income = serializers.IntegerField()
