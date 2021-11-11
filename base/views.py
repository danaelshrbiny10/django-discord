from django.shortcuts import render
from .models import Room



# rooms = [
#     {'id':1 , 'name':'backend developers!'},
#     {'id':2 , 'name':'frontend developers!'},
#     {'id':3 , 'name':'graphic designer!'},
#     {'id':4 , 'name':'fullstack developers!'},
# ]



def homePage(request):
    rooms = Room.objects.all()
    context ={'rooms':rooms}
    return render(request, 'base/home.html',context)


def room(request,pk):
    # room = None
    # for i in rooms:
    #     if i["id"] ==int(pk):
    #         room = i
    room = Room.objects.get(id=pk)
    context = {'room':room}
    return render(request, 'base/room.html',context)
