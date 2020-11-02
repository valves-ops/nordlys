from rest_framework import status
from rest_framework.response import Response


def check_for_missing_parameters(parameters, payload):
    for parameter in parameters:
        if parameter not in payload:
            content = {"detail": "Missing parameter " + parameter}
            return Response(content, status=status.HTTP_400_BAD_REQUEST)