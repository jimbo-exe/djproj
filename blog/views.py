from multiprocessing import context
from django.shortcuts import render
from .models import Post
#from django.http import HttpResponse

posts = [
	#dummy posts
	{
		'author' : 'Atin Arora',
		'title' : 'Post 1',
		'content' : 'Mera balam thanedar',
		'date_posted' : '26/8/2022'
	},
	{
		'author' : 'NBA Leader',
		'title' : 'Post 69',
		'content' : 'I play NB',
		'date_posted' : '27/8/2022'
	},
]	


def home(request):
	context = {
		'title' : 'Home',
		'posts' : Post.objects.all(),
	}
	return render(request, 'blog/home.html', context)

def about(request):
#	return HttpResponse('<h1>Blog About</h1>')
	return render(request, 'blog/about.html')
