from rest_framework.views import APIView
from rest_framework.response import Response


class HelloAPIView(APIView):
    """Test API View"""

    def get(self,request,format=None):
        """Returns a list of API features"""
        an_apiview=[
            'Uses HTTP Methods as function (get , post ,patch,put , delete)',
            'Is similar to a traditionl Django view',
            'Gives you the m,ost control over your application logic',
            'Is mapped manually to URLS',
        ]

        return Response({'message':'Hello','an API View':an_apiview})
