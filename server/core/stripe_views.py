from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.conf import settings
from utils.validation import check_for_missing_parameters


# Stripe Level Control
class GetStripe(APIView):
    def get(self, request, pk):
        print(pk)
        pk = int(pk)
        stripe = settings.RELAY.stripes[pk]
        content = {
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
        return Response(content, status=status.HTTP_200_OK)


class SetPixelColor(APIView):
    def put(self, request, pk):
        pk = int(pk)
        check_for_missing_parameters(["pixel_number", "color"], request.data)
        settings.RELAY.stripes[pk].set_pixel_color(
            request.data["pixel_number"], tuple(request.data["color"])
        )
        return Response(status=status.HTTP_200_OK)


class Show(APIView):
    def put(self, request, pk):
        pk = int(pk)
        settings.RELAY.stripes[pk].show()
        return Response(status=status.HTTP_200_OK)


class SetSegmentColor(APIView):
    def put(self, request, pk):
        pk = int(pk)
        check_for_missing_parameters(
            ["segment_position", "segment_length", "color"], request.data
        )
        settings.RELAY.stripes[pk].set_segment_color(
            request.data["segment_position"],
            request.data["segment_length"],
            request.data["color"],
        )
        return Response(status=status.HTTP_200_OK)
