from multiprocessing import context
from django.shortcuts import render
#from django.http import HttpResponse

posts = [
	{
		'author' : 'Atin Arora',
		'title' : 'Post 1',
		'content' : 'Mera balam thanedar',
		'date_posted' : '26/8/2022'
	},
	{
		'author' : 'Nadu Man',
		'title' : 'Post 69',
		'content' : 'I love sutta',
		'date_posted' : '27/8/2022'
	},
]	
	

def home(request):
	context = {
		'title' : 'Home',
		'posts' : posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
#	return HttpResponse('<h1>Blog About</h1>')
	return render(request, 'blog/about.html')
