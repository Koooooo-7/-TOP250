from django.shortcuts import render

# Create your views here.
from douban_app.models import  Douban
def home(request):
    #select * from douban where id=1
   # print(Douban.objects.get(id=1).title)
    info=Douban.objects.filter().order_by('?')[:10]  #fliter 可迭代对象 order_by? 随机[:4]取4个
    for i in info:
        print(i.title)
    context={
       # 'nums':[x for x in range(10)],
        'infos':info

    }

    return  render(request,"douban_app/index.html",context=context)
