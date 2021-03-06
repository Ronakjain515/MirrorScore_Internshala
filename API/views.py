from datetime import datetime
from datetime import date
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class ping(APIView):
    def get(self, request):
        return Response({"status": "OK"})


class task(APIView):
    def get(self, request):
        try:
            dateData = int(request.GET.get("date"))
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        dt_object = datetime.fromtimestamp(dateData)
        if dt_object.date() == date.today():
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
