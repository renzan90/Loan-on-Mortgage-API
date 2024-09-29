from rest_framework import serializers
from loans.models import Loan

class LoanSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'