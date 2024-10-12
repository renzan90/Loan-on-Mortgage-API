import re
from .models import *
import base64
from cryptography.fernet import Fernet
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

key = Fernet.generate_key()
cipher = Fernet(key)

class BorrowerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields = '__all__'
    
    def validate_ph_no(self, value):
        if len(value) != 10:
            raise ValidationError("Phone number needs to be 10 digit")
        return value
    
    def validate_email(self, email):
        
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

        if not re.match(pattern, email):
            raise ValidationError("Please input a proper email ID")
        
        return email
    
    def create(self, validated_data):
        """To encrypt user email and phone number"""

        email = validated_data['email']
        encrypted_email = cipher.encrypt(email.encode()).decode()

        phone = validated_data['ph_no']
        encrypted_phone = cipher.encrypt(phone.encode()).decode()

        borrower = Borrower.objects.create(
            borrower_id = validated_data['borrower_id'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            profession = validated_data['profession'],
            email = encrypted_email,
            ph_no = encrypted_phone,
            date_of_birth = validated_data['date_of_birth']
        )

        borrower.save()

        return borrower

    
class BankDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankDetails
        fields = '__all__'

class KYCSerializer(serializers.ModelSerializer):
    class Meta:
        model = KYC
        fields = '__all__'

class IncomeDocsSerializer(serializers.ModelSerializer):
    class Meta:
        model = IncomeDocs
        fields = '__all__'