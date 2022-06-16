from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from .import forms 

def post_list(request):

 def post_detail(requset, text):

  @login_required(login_url="/accounts/login/")
  def post_create(request):
   if request.method == 'POST':
     form = forms.CreatePost(request.POST,request.FILES)
     if form.is_valid():
        #save post to db
        instance = form.save(commit=False)
        instance.author = request.user
        instance.save
        return redirect('posts:list')
   else:
     form = forms.CreatePost()
   return render(request, 'posts/post_create.html',{'form':form}) 

      
