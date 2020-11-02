from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.conf import settings


def check_for_missing_parameters(parameters, payload):
    for parameter in parameters:
        if parameter not in payload:
            content = {"detail": "Missing parameter " + parameter}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)


class AddStripe(APIView):
    def post(self, request):
        check_for_missing_parameters(["numpixels", "pin"], request.data)
        settings.RELAY.add_stripe(request.data["numpixels"], request.data["pin"])
        return Response(status=status.HTTP_200_OK)


class SetPixelColor(APIView):
    def post(self, request):
        check_for_missing_parameters(["pixel_number", "color"], request.data)

        settings.RELAY.set_pixel_color(
            request.data["pixel_number"], tuple(request.data["color"])
        )
        return Response(status=status.HTTP_200_OK)


class Show(APIView):
    def post(self, request):
        settings.RELAY.show()
        return Response(status=status.HTTP_200_OK)


class SetSegmentColor(APIView):
    def post(self, request):
        check_for_missing_parameters(
            ["segment_position", "segment_length", "color"], request.data
        )
        settings.RELAY.set_segment_color(
            request.data["segment_position"],
            request.data["segment_length"],
            request.data["color"],
        )
        return Response(status=status.HTTP_200_OK)
