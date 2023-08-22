from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
from rest_framework.response import Response
from datetime import datetime


class CustomRetrieveAPIView(APIView):

    # cache this endpoint for 10 seconds
    @method_decorator(cache_page(10))
    def get(self, request, *args, **kwargs):

        # We can modify and write here comprehensive SQL queries and other statements
        # to prepare a response
        # For Example:
        #
        # u1 = User.objects.get(id=kwargs.get('id'))
        # return Response({'name': u1.name, 'age': u1.age})

        return Response({'timestamp': str(datetime.now())})