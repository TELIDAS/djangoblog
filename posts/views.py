from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from posts.models import Post


@csrf_exempt
def get_posts(request):
    method_post = request.method
    if method_post == 'POST':
        post = Post.objects.create(title="Good Morning", description="Have a good day")
        return HttpResponse('Put the information to my profile')
    if method_post == 'GET':
        saved_posts = Post.objects.all()
        return HttpResponse(saved_posts)
    if method_post == 'DELETE':
        post = Post.objects.get(pk=1)
        post.delete()
        return HttpResponse('Post deleted')
    if method_post in ['PUT', 'PATCH']:
        post = Post.objects.create(title='Good Morning', description='Have a good day')
        post.title = "Good evening"
        post.description = "Good night"
        post.save()

    # print(vars(HttpResponse))
    return HttpResponse('Hi master, i\'m working!')

@csrf_exempt
def get_profile(request):
    method_profile = request.method
    print(method_profile)
    if method_profile == 'POST':
        return HttpResponse('Post on my profile')
    if method_profile == 'PUT':
        return HttpResponse('Put the information to my profile')
    if method_profile == 'GET':
        return HttpResponse('Get the information from my profile')
    if method_profile == 'DELETE':
        return HttpResponse('Delete my profile')
    if method_profile == 'PATCH':
        return HttpResponse('New profile patch is available')
    return HttpResponse('My profile')
