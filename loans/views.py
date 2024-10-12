from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView
from loans.models import Loans
from loans.serializers import LoanSerializer, EligibilityFormSerializer
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from .tasks import calculate_eligibility

eligibility_result = None

class LoanViewSet(ViewSet):

    global eligibility_result
    
    def list(self, request, *args, **kwargs):
        queryset = Loans.objects.all()
        serialized_data = LoanSerializer(queryset, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
    
    @action(detail=False, methods=['get', 'post'])
    def same_amount_loans(self, request):
        queryset = Loans.objects.filter(amount=request.query_params.get('amount'))
        if queryset.exists():
            loan = queryset.first()
        else:
            return Response({'result':'items not found'}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EligibilityFormSerializer(request.data)
        if serializer.is_valid(raise_exception=True):
            real_estate = serializer.validated_data['real_estate']
            other_mortgageables = serializer.validated_data['other_mortgageables']
            property_valuation = serializer.validated_data['property_valuation']
            taxable_annual_income = serializer.validated_data['taxable_annual_income']
        
        eligibility_result = calculate_eligibility.delay(
            real_estate, 
            other_mortgageables,
            property_valuation, 
            taxable_annual_income, 
            loan
        )                                        

        return Response({'result':eligibility_result}, status=status.HTTP_200_OK)
