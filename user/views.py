from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import *
from .serializers import *
from loans.views import eligibility_result


class BorrowerCreateAPIView(APIView):
    authentication_classes = []
    permission_classes = []
    renderer_classes = []
    parser_classes = []

    def post(self, request):
        
        if eligibility_result == None:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        queryset = Borrower.objects.create(data=request.data)
        serialized_object =  BorrowerSerializers(queryset)
        if serialized_object.is_valid():
            serialized_object.save()
            return Response(serialized_object, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk=None):
        
        data = get_object_or_404(borrower_id=pk)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

