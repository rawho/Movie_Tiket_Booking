from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *
# Create your views here.
def Home(request):
    data = Movie.objects.all()
    d = {'data':data}
    return render(request,'carousel.html',d)

def Admin_Home(request):
    total_user=0
    total_movie=0
    total_booking=0
    for i in Movie.objects.all():
        total_movie+=1
    for i in Booking.objects.all():
        total_booking+=1
    d = {'total_user':total_user,'total_movie':total_movie,'total_booking':total_booking}
    return render(request,'admin_dash.html',d)




def Add_Movie(request):
    error = False
    if request.method == 'POST':
        n = request.POST['name']
        Movie.objects.create(
            name = n,
        )
        error = True
    d = {
        'error': error,
    }
    return render(request,'add_movie.html',d)


def delete_movie(request,pid):
    data = Movie.objects.get(id=pid)
    data.delete()
    return redirect('home')

def Movie_detail(request,pid):
    data = Movie.objects.get(id=pid)
    time1 = Movie_Time.objects.all()
    if request.method=="POST":
        t = request.POST['time']
        d = request.POST['date']
        if request.user:
            data1 = Set_Timing.objects.create(
                time1=t,
                date1=d,
                movie=data
            )
        else:
            return redirect('home')
        return redirect('book_ticket',data1.id)
    d = {'data':data,'time1':time1}
    return render(request,'movie_detail.html',d)



def Book_Ticket(request,pid):
    data = Set_Timing.objects.get(id=pid)
    data1 = Booking.objects.filter(set_time=data)
    data2 = Pending.objects.filter(set_time=data)

    li = ""
    for i in data1:
        li+=","+i.seat
    
    li2 = ""
    for i in data2:
        li2+=","+i.seat
    print(li2)
    error = False
    
    book=""
    pend=""
    movie_time = Movie_Time.objects.all()
    if request.method=="POST":
        try:
            n = request.POST['num']
            s = request.POST['seat']
            p = int(n)*120
            book = Booking.objects.create(set_time=data,ticket=n,price=p,seat=s)
        except:
            pass
        try:
            n_pending = request.POST['num_pending']
            s_pending = request.POST['seat_pending']
            p_pending = int(n_pending)*120
            pend = Pending.objects.create(set_time=data,ticket=n_pending,price=p_pending,seat=s_pending)
        
        except:
            pass

        error=True
    # d = {'data':data,'error':error,'li':li,'li2':li2,'book':book, 'pend' : pend}

    if pid == 1:
        movies = {}
        movies["name"] = Movie.objects.filter(screen=1)
        print(movies)
           
        d = {'data':data,'error':error,'li':li,'li2':li2,'book':book, 'pend' : pend,'movies':movies, 'movie_time':movie_time}
         
        return render(request,'book_ticket1.html',d)


    if pid == 1:
        return render(request,'book_ticket1.html', d)
    elif pid == 2:
        return render(request, 'book_ticket2.html', d)
    elif pid == 3:
        movie = Movie.objects.filter(screen=3)
        print(movie)
        return render(request, 'book_ticket3.html', d)
    elif pid == 4:
        return render(request, 'book_ticket4.html', d)
    elif pid == 5:
        return render(request, 'book_ticket5.html', d)

def View_Booking(request):
    user = User.objects.get(id=request.user.id)
    cust = Customer.objects.get(user=user)
    data = Booking.objects.filter(user1=cust)
    d = {'data':data}
    return render(request,'view_booking.html',d)


def All_Booking(request):
    data = Booking.objects.all()
    d = {'data': data}
    return render(request,'all_booking.html',d)


def delete_booking1(request,pid):

    data = Booking.objects.get(id=pid)
    data.delete()
    return redirect('all_booking')

def delete_booking(request,pid):

    data = Booking.objects.get(id=pid)
    data.delete()
    return redirect('view_booking')


