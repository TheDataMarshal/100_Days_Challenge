from django.shortcuts import render

posts = [
	{
		'author': 'The Data Marshal',
		'title': 'Blog post 1',
		'content': 'First post content',
		'date_posted': 'February 10, 2021'
	},
	{
		'author': 'Some other Author',
		'title': 'Blog post 2',
		'content': 'Second post content',
		'date_posted': 'February 01, 2021'
	}

]

def home(request):
	context = {
		'posts' : posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
    return render(request,'blog/about.html', {'title':'About'})
