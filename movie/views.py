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
        screens=[1,2,3,4,5]
        A=['A1','A2','A3','A4','A5']
        B=['B1','B2','B3','B4','B5','B6']
        C=['C1','C2','C3','C4','C5','C6','C7','C8']
        D=['D1','D2','D3','D4','D5','D6','D7','D8']
        E=['E1','E2','E3','E4','E5','E6','E7','E8','E9'] 
        F=['F1','F2','F3','F4','F5','F6','F7','F8','F9']
        G=['G1','G2','G3','G4','G5','G6','G7','G8']
        H=['H1','H2','H3','H4','H5','H6','H7','H8','H9']
        I=['I1','I2','I3','I4','I5','I6','I7','I8','I9']
        J=['J1','J2','J3','J4','J5','J6','J7','J8']
        K=['K1','K2','K3','K4','K5','K6','K7','K8']
        d = {
            'data':data,
            'error':error,
            'li':li,'li2':li2,
            'book':book, 
            'pend' : pend,
            'movies':movies,
            'movie_time':movie_time,
            'screens':screens,
            'A':A,'B':B,'C':C,'D':D,'E':E,'F':F,'G':G,'H':H,'I':I,'J':J,'K':K
            }
         
        return render(request,'book_ticket1.html',d)
    elif pid == 2:
        movies = {}
        movies["name"] = Movie.objects.filter(screen=2)
        print(movies)
           
        d = {'data':data,'error':error,'li':li,'li2':li2,'book':book, 'pend' : pend,'movies':movies, 'movie_time':movie_time}
        return render(request, 'book_ticket2.html', d)
    elif pid == 3:
        movies = {}
        movies["name"] = Movie.objects.filter(screen=3)
        print(movies)
           
        d = {'data':data,'error':error,'li':li,'li2':li2,'book':book, 'pend' : pend,'movies':movies, 'movie_time':movie_time}
        return render(request, 'book_ticket3.html', d)
    elif pid == 4:
        movies = {}
        movies["name"] = Movie.objects.filter(screen=4)
        print(movies)
           
        d = {'data':data,'error':error,'li':li,'li2':li2,'book':book, 'pend' : pend,'movies':movies, 'movie_time':movie_time}
        return render(request, 'book_ticket4.html', d)
    elif pid == 5:
        movies = {}
        movies["name"] = Movie.objects.filter(screen=5)
        print(movies)
           
        d = {'data':data,'error':error,'li':li,'li2':li2,'book':book, 'pend' : pend,'movies':movies, 'movie_time':movie_time}
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


