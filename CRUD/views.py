from django.shortcuts import redirect,render
from APP.models import News
def INDEX(request):
    news=News.objects.all()

    context={
        'news':news,
    }

    return render(request,'index.html',context)


def ADD(request):
    if request.method=="POST":
        title=request.POST.get('title')
        news_details=request.POST.get('news_details')

        news =News(
            title = title,
            news_details = news_details
           
        ) 
        news.save()
        return redirect('home')

    return render(request,'index.html')
def EDIT(request):
    news=News.objects.all()

    context = {
        'news':news,
    }

    return redirect(request,'index.html',context)

def UPDATE(request,id):
    if request.method == "POST":
        title=request.POST.get('title')
        
        news_details=request.POST.get('news_details')
       
        news = News(
            id=id,
            title = title,
            news_details=news_details
           
    )
        news.save()
        return redirect('home')
    return redirect(request,'index.html')

def DELETE(request,id):
    news=News.objects.filter(id=id)
    news.delete()
    context={
        'news':news,

    }
    return redirect("home")