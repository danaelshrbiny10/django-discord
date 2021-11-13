from django.shortcuts import redirect, render
from .models import Room
from .forms import RoomForm


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


def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        # print(request.POST)
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    context ={'form':form}
    return render(request, 'base/room_form.html',context)


def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST ,instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')
    
    context ={'form':form}
    return render(request, 'base/room_form.html',context)


def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html' , {'obj':room})