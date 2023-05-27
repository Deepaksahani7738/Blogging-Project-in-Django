from django.shortcuts import render,HttpResponse,get_object_or_404
from .models import BlogPost
from .forms import PostBlogForm,RegistrationForm
from django.utils import timezone
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def index(request):
    result=BlogPost.objects.all().order_by('-id')
    # return HttpResponse(result)
    content={'response':result}
    return render(request,'blog/index.html',content)


@login_required(login_url='login')
def post_detail_views(request,pk):
    post_result=get_object_or_404(BlogPost,pk=pk)
    content={'post':post_result}
    return render(request,'blog/post_detail.html',content)



def post_new(request):
    if request.method=='POST':
        form_data=PostBlogForm(request.POST)
        data=BlogPost.objects.all()
        if form_data.is_valid():
            post_data=form_data.save(commit=False)
            post_data.author=request.user
            post_data.create_date=timezone.now()
            post_data.publish_date=timezone.now()
            post_data.save()
            messages.success(request,'Data has been Successfuly')
            return redirect('home')
    else:
        form_data=PostBlogForm()
        messages.error(request,form_data.errors)
    return render(request,'blog/post_new.html',{'form_data':form_data})

def post_edit(request,pk):
    post_data=get_object_or_404(BlogPost,pk=pk)
    if request.method=='POST':
        form_data=PostBlogForm(request.POST,instance=post_data)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,'Data Updates Successfully')
            return redirect('home')
    else:
        form_data=PostBlogForm(instance=post_data)
    return render(request,'blog/post_edit.html',{'form_data':form_data})

def post_delete(request,pk):
    post_data=get_object_or_404(BlogPost,pk=pk)
    post_data.delete()
    messages.info(request,'Post Delete Successfully')
    return redirect('home')


def register(request):
    if request.method=='GET':
        form=RegistrationForm()
        return render(request,'register.html',{'form':form})
    
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,'Account was Successfuly created for '+username)
            return redirect('home')
        else:
            messages.error(request,'Error in Processing Your request')
            return render(request,'register.html',{'form':form})
    
    return render(request,'register.html',{'form':form})



    # if request.method=='POST':
    #     form=RegistrationForm(request.POST)
    # return render(request,'register.html',{'form':form})