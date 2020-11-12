from django.http import JsonResponse
from django.shortcuts import render

from posting.models import Post


def my_view(request):
    posts = Post.objects.all().values('id','text')
    return JsonResponse(list(posts),safe = False)
