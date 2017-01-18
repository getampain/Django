from django.shortcuts import render

# Create your views here.

def post_list(request):
	return render(request, 'app/post_list.html',{})
def test_page(request):
	return render(request, 'app/test.html',{})

