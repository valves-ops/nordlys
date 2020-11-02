from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.conf import settings
import sys
from neopyxel.effects import Fireplace
from collections.abc import Iterable
from utils.validation import check_for_missing_parameters


# Relay Level Control
class AddStripe(APIView):
    def post(self, request):

        if isinstance(request.data, Iterable):
            stripes = request.data
        else:
            stripes = [request.data]
        print(stripes)
        for stripe in stripes:
            check_for_missing_parameters(["numpixels", "pin"], stripe)
            settings.RELAY.add_stripe(stripe["numpixels"], stripe["pin"])
        return Response(status=status.HTTP_200_OK)


class GetStripes(APIView):
    def get(self, request):
        stripes = []
        for stripe in settings.RELAY.stripes:
            stripes.append(
                {
                    "id": stripe.stripe_number,
                    "num_pixels": stripe.num_pixels,
                    "pin": stripe.pin,
                    "pixels": [
                        {
                            "displayed_color": pixel.displayed_color,
                            "buffer_color": pixel.buffer_color,
                        }
                        for pixel in stripe.pixels
                    ],
                }
            )
        return Response(stripes, status=status.HTTP_200_OK)


class FlushStripes(APIView):
    def post(self, request):
        settings.RELAY.flush_stripes()
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


class ExecuteEffectFireplace(APIView):
    def post(self, request):
        settings.RELAY.execute_effect(Fireplace)
        return Response(status=status.HTTP_200_OK)


class StopEffect(APIView):
    def post(self, request):
        settings.RELAY.stop_effect()
        return Response(status=status.HTTP_200_OK)
