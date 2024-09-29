from rest_framework.viewsets import Viewset
from loans.models import Loans
from loans.serializer import LoanSerializer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK
from django.shortcuts import get_object_or_404

def LoanViewset(viewset):

    def list(self, request, *args, **kwargs):
        queryset = Loans.objects.all()
        serialized_data = LoanSerializer(queryset, many=True)
        return Response(serialized_data.data, status=HTTP_200_OK)
    
    def retrieve(self, request, pk):
        queryset = Loans.objects.all()
        object = get_object_or_404(queryset, pk)
        serialized_data = LoanSerializer(object)
        return Response(serialized_data.data, status=HTTP_200_OK)
    

