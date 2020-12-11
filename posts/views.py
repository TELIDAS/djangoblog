from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from posts.models import Post, Profile


@csrf_exempt
def get_posts(request):
    method_post = request.method
    if method_post == 'POST':
        post = Post.objects.create(title="Good Morning", description="Have a good day")
        return HttpResponse('Put the information to my posts')
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
        profile = Profile.objects.create(name='Arata', sex='male', age=23, hobby='reading books')
        return HttpResponse('Created new profile')
    if method_profile in ['PUT', 'PATCH']:
        profile = Profile.objects.create(name='Arata', sex='male', age=23, hobby='reading books')
        profile.name = "Miko"
        profile.age = 19
        profile.sex = 'female'
        profile.hobby = 'dancing'
        profile.save()
        return HttpResponse('Put the information to my profile')
    if method_profile == 'GET':
        saved_profile = Profile.objects.all()
        return HttpResponse(saved_profile)
    if method_profile == 'DELETE':
        profile = Profile.objects.get(pk=int())
        profile.delete()
        return HttpResponse('Profile deleted')
    return HttpResponse('My profile')
