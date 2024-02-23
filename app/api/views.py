from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
import traceback


def api(request):
    try:
        contexts = dict()
        # 現在ログインしている?
        contexts['user'] = None
        return render(request, 'api/index.html', contexts)

    except Exception as e:
        traceback.print_exc()
        result = {"code": 404, "message": "NG"}
        return Response(result, status=status.HTTP_404_NOT_FOUND)
