from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *
import dateutil.parser as dp
# Create your views here.
timings=[
    '2021-01-01 09:00:00.999Z','2021-01-01 12:00:00.999Z','2021-01-01 15:00:00.999Z','2021-01-01 18:00:00.999Z','2021-01-01 21:00:00.999Z'
]
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
    data1 = Booking.objects.filter(time=timings[1])
    data2 = Pending.objects.filter(time=timings[1])
    _P=['P1','P2','P3','P4','P5','P6','P7','P8','P9','P10','P11','P12','P13','P14','P15','P16','P17','P18','P19','P20','P21','P22','P23','P24','P25','P26']
    _Q=['Q1','Q2','Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20','Q21','Q22','Q23','Q24','Q25','Q26']
    _R=['R1','R2','R3','R4','R5','R6','R7','R8','R9','R10','R11','R12','R13','R14','R15','R16','R17','R18','R19','R20','R21','R22','R23','R24','R25','R26','R27','R28','R29']
    li = []
    for i in data1:
        li.append(i.seat)
    li2 = []
    for i in data2:
        li2.append(i.seat)
    error = False
    
    book=""
    pend=""
    p=0
    movie_time = Movie_Time.objects.all()
    if request.method=="POST":
        
        try:
            p=int()
            time=request.POST['time']
            if time[-2:]=='PM' and time[:2]!='12':
               time=str(int(time[:2])+12)          
            else:
                time=time[:2]
            date_time= dp.parse(str('2021-01-01T'+time+':00:00.999Z' ))
            print(date_time)
            n = request.POST['num']
            s = request.POST['seat']

            _s=s.split(",")
            if pid == 2 or pid == 3 :
                for i in _s:
                        if i in _P or i in _Q or i in _R:
                            p=p+150
                        else:
                            p=p+120
                print(p)   
            else:
                p = int(n)*120
                print(p)
            for i in _s:
                book = Booking.objects.create(set_time=data,time=date_time,ticket=1,price=p,seat=i)
        except:
            pass
        try:
            n_pending = request.POST['num_pending']
            s_pending = request.POST['seat_pending']
            
            p_pending = int(n_pending)*120
            pend_seat = s_pending.split(',')
            print(pend_seat)
          
            for i in pend_seat:
                print(i)
                print('pending')
                pend = Pending.objects.create(set_time=data,ticket=n_pending,price=p_pending,seat=i)
                print(pend)
        except:
            if request.POST['num_unpending']:
                n_unpending = request.POST['num_unpending']
                s_unpending = request.POST['seat_unpending']


                print(n_unpending, s_unpending)
                print('unpending: ' + s_unpending)
                unpend_seat = s_unpending.split(',')
                for j in unpend_seat:
                    Pending.objects.filter(seat__icontains = j).delete()


        error=True
    # d = {'data':data,'error':error,'li':li,'li2':li2,'book':book, 'pend' : pend}
    
    if pid == 1:
        movies = {}
        movies["name"] = Movie.objects.filter(screen=1)
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
        row=[1,2,3,4,5,6,7,8,9]
        seats={'A':A,'B':B,'C':C,'D':D,'E':E,'F':F,'G':G,'H':H,'I':I,'J':J,'K':K}
        d = {
            'data':data,
            'error':error,
            'li':li,'li2':li2,
            'price': p,
            'book':book, 
            'pend' : pend,
            'movies':movies,
            'movie_time':movie_time,
            'screens':screens,
            'seats':seats,
            'row':row
            }
         
        return render(request,'book_ticket1.html',d)
    elif pid == 2:
        movies = {}
        movies["name"] = Movie.objects.filter(screen=2)
        screens=[1,2,3,4,5]
        A=['A1','A2','A3','A4','A5','A6']
        B=['B1','B2','B3','B4','B5','B6','B7']
        C=['C1','C2','C3','C4','C5','C6','C7']
        D=['D1','D2','D3','D4','D5','D6','D7','D8','D9','D10','D11','D12','D13','D14','D15','D16','D17','D18','D19','D20','D21','D22','D23','D24','D25','D26','D27','D28']
        E=['E1','E2','E3','E4','E5','E6','E7','E8','E9','E10','E11','E12','E13','E14','E15','E16','E17','E18','E19','E20','E21','E22','E23','E24','E25','E26'] 
        F=['F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12','F13','F14','F15','F16','F17','F18','F19','F20','F21','F22','F23','F24','F25','F26']
        G=['G1','G2','G3','G4','G5','G6','G7','G8','G9','G10','G11','G12','G13','G14','G15','G16','G17','G18','G19','G20','G21','G22','G23','G24','G25','G26']
        H=['H1','H2','H3','H4','H5','H6','H7','H8','H9','H10','H11','H12','H13','H14','H15','H16','H17','H18','H19','H20','H21','H22','H23','H24','H25','H26']
        I=['I1','I2','I3','I4','I5','I6','I7','I8','I9','I10','I11','I12','I13','I14','I15','I16','I17','I18','I19','I20','I21','I22','I23','I24','I25','I26']
        J=['J1','J2','J3','J4','J5','J6','J7','J8','J9','J10','J11','J12','J13','J14','J15','J16','J17','J18','J19','J20','J21','J22','J23','J24','J25','J26']
        K=['K1','K2','K3','K4','K5','K6','K7','K8','K9','K10','K11','K12','K13','K14','K15','K16','K17','K18','K19','K20','K21','K22','K23','K24','K25','K26']
        L=['L1','L2','L3','L4','L5','L6','L7','L8','L9','L10','L11','L12','L13','L14','L15','L16','L17','L18','L19','L20','L21','L22','L23','L24','L25','L26']
        M=['M1','M2','M3','M4','M5','M6','M7','M8','M9','M10','M11','M12','M13','M14','M15','M16','M17','M18','M19','M20','M21','M22','M23','M24','M25','M26']
        N=['N1','N2','N3','N4','N5','N6','N7','N8','N9','N10','N11','N12','N13','N14','N15','N16','N17','N18','N19','N20','N21','N22','N23','N24','N25','N26']
        O=['O1','O2','O3','O4','O5','O6','O7','O8','O9','O10','O11','O12','O13','O14','O15','O16','O17','O18','O19','O20','O21','O22','O23','O24','O25','O26']
        P=['P1','P2','P3','P4','P5','P6','P7','P8','P9','P10','P11','P12','P13','P14','P15','P16','P17','P18','P19','P20','P21','P22','P23','P24','P25','P26']
        Q=['Q1','Q2','Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20','Q21','Q22','Q23','Q24','Q25','Q26']
        R=['R1','R2','R3','R4','R5','R6','R7','R8','R9','R10','R11','R12','R13','R14','R15','R16','R17','R18','R19','R20','R21','R22','R23','R24','R25','R26','R27','R28','R29']
        row=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]
        seats={'A':A,'B':B,'C':C,'D':D,'E':E,'F':F,'G':G,'H':H,'I':I,'J':J,'K':K,'L':L,'M':M,'N':N,'O':O,'P':P,'Q':Q,'R':R}
        d = {
            'data':data,
            'error':error,
            'li':li,'li2':li2,
            'price': p,
            'book':book, 
            'pend' : pend,
            'movies':movies,
            'movie_time':movie_time,
            'screens':screens,
            'seats':seats,
            'row':row
            }
        return render(request, 'book_ticket2.html', d)
    elif pid == 3:
        movies = {}
        movies["name"] = Movie.objects.filter(screen=3)
        screens=[1,2,3,4,5]
        A=['A1','A2','A3','A4','A5','A6','A7','A8','A9']
        B=['B1','B2','B3','B4','B5','B6','B7','B8','B9','B10']
        C=['C1','C2','C3','C4','C5','C6','C7','C8','C9','C10']
        D=['D1','D2','D3','D4','D5','D6','D7','D8','D9','D10','D11','D12','D13','D14','D15','D16','D17','D18','D19','D20','D21','D22','D23','D24','D25','D26','D27','D28','D29','D30','D31','D32']
        E=['E1','E2','E3','E4','E5','E6','E7','E8','E9','E10','E11','E12','E13','E14','E15','E16','E17','E18','E19','E20','E21','E22','E23','E24','E25','E26','E27','E28','E29','E30'] 
        F=['F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12','F13','F14','F15','F16','F17','F18','F19','F20','F21','F22','F23','F24','F25','F26','F27','F28','F29','F30']
        G=['G1','G2','G3','G4','G5','G6','G7','G8','G9','G10','G11','G12','G13','G14','G15','G16','G17','G18','G19','G20','G21','G22','G23','G24','G25','G26','G27','G28','G29','G30']
        H=['H1','H2','H3','H4','H5','H6','H7','H8','H9','H10','H11','H12','H13','H14','H15','H16','H17','H18','H19','H20','H21','H22','H23','H24','H25','H26','H27','H28','H29','H30']
        I=['I1','I2','I3','I4','I5','I6','I7','I8','I9','I10','I11','I12','I13','I14','I15','I16','I17','I18','I19','I20','I21','I22','I23','I24','I25','I26','I27','I28','I29','I30']
        J=['J1','J2','J3','J4','J5','J6','J7','J8','J9','J10','J11','J12','J13','J14','J15','J16','J17','J18','J19','J20','J21','J22','J23','J24','J25','J26','J27','J28','J29','J30']
        K=['K1','K2','K3','K4','K5','K6','K7','K8','K9','K10','K11','K12','K13','K14','K15','K16','K17','K18','K19','K20','K21','K22','K23','K24','K25','K26','K27','K28','K29','K30']
        L=['L1','L2','L3','L4','L5','L6','L7','L8','L9','L10','L11','L12','L13','L14','L15','L16','L17','L18','L19','L20','L21','L22','L23','L24','L25','L26','L27','L28','L29','L30']
        M=['M1','M2','M3','M4','M5','M6','M7','M8','M9','M10','M11','M12','M13','M14','M15','M16','M17','M18','M19','M20','M21','M22','M23','M24','M25','M26','M27','M28','M29','M30']
        N=['N1','N2','N3','N4','N5','N6','N7','N8','N9','N10','N11','N12','N13','N14','N15','N16','N17','N18','N19','N20','N21','N22','N23','N24','N25','N26','N27','N28','N29','N30']
        O=['O1','O2','O3','O4','O5','O6','O7','O8','O9','O10','O11','O12','O13','O14','O15','O16','O17','O18','O19','O20','O21','O22','O23','O24','O25','O26','O27','O28','O29','O30']
        P=['P1','P2','P3','P4','P5','P6','P7','P8','P9','P10','P11','P12','P13','P14','P15','P16','P17','P18','P19','P20','P21','P22','P23','P24','P25','P26','P27','P28','P29','P30']
        Q=['Q1','Q2','Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q10','Q11','Q12','Q13','Q14','Q15','Q16','Q17','Q18','Q19','Q20','Q21','Q22','Q23','Q24','Q25','Q26','Q27','Q28','Q29','Q30']
        R=['R1','R2','R3','R4','R5','R6','R7','R8','R9','R10','R11','R12','R13','R14','R15','R16','R17','R18','R19','R20','R21','R22','R23','R24','R25','R26','R27','R28','R29','R30','R31','R32','R33']
        row=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33]
        seats={'A':A,'B':B,'C':C,'D':D,'E':E,'F':F,'G':G,'H':H,'I':I,'J':J,'K':K,'L':L,'M':M,'N':N,'O':O,'P':P,'Q':Q,'R':R}
        d = {
            'data':data,
            'error':error,
            'li':li,'li2':li2,
            'price': p,
            'book':book, 
            'pend' : pend,
            'movies':movies,
            'movie_time':movie_time,
            'screens':screens,
            'seats':seats,
            'row':row
            }
        return render(request, 'book_ticket3.html', d)
    elif pid == 4:
        movies = {}
        movies["name"] = Movie.objects.filter(screen=4)
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
        
        row=[1,2,3,4,5,6,7,8,9]
        seats={'A':A,'B':B,'C':C,'D':D,'E':E,'F':F,'G':G,'H':H,'I':I,'J':J,'K':K}
        d = {
            'data':data,
            'error':error,
            'li':li,'li2':li2,
            'price': p,
            'book':book, 
            'pend' : pend,
            'movies':movies,
            'movie_time':movie_time,
            'screens':screens,
            'seats':seats,
            'row':row
            }
        return render(request, 'book_ticket4.html', d)
    elif pid == 5:
        movies = {}
        movies["name"] = Movie.objects.filter(screen=5)
        screens=[1,2,3,4,5]
        A=['A1','A2','A3','A4','A5','A6','A7']
        B=['B1','B2','B3','B4','B5','B6','B7','B8']
        C=['C1','C2','C3','C4','C5','C6','C7','C8']
        D=['D1','D2','D3','D4','D5','D6','D7','D8','D9','D10','D11','D12']
        E=['E1','E2','E3','E4','E5','E6','E7','E8','E9','E10','E11','E12']
        F=['F1','F2','F3','F4','F5','F6','F7','F8','F9','F10','F11','F12']
        G=['G1','G2','G3','G4','G5','G6','G7','G8','G9','G10','G11','G12']
        H=['H1','H2','H3','H4','H5','H6','H7','H8','H9','H10','H11','H12']
        I=['I1','I2','I3','I4','I5','I6','I7','I8','I9','I10','I11','I12']
        J=['J1','J2','J3','J4','J5','J6','J7','J8','J9','J10','J11','J12']
        K=['K1','K2','K3','K4','K5','K6','K7','K8','K9','K10','K11','K12']
        L=['L1','L2','L3','L4','L5','L6','L7','L8','L9','L10','L11','L12']
        M=['M1','M2','M3','M4','M5','M6','M7','M8','M9','M10','M11','M12']
        N=['N1','N2','N3','N4','N5','N6','N7','N8','N9','N10','N11','N12']
        O=['O1','O2','O3','O4','O5','O6','O7','O8','O9','O10','O11','O12']
        P=['P1','P2','P3','P4','P5','P6','P7','P8','P9','P10','P11','P12']
        row=[1,2,3,4,5,6,7,8,9,10,11,12]
        seats={'A':A,'B':B,'C':C,'D':D,'E':E,'F':F,'G':G,'H':H,'I':I,'J':J,'K':K,'L':L,'M':M,'N':N,'O':O,'P':P}
        d = {
            'data':data,
            'error':error,
            'li':li,'li2':li2,
            'price': p,
            'book':book, 
            'pend' : pend,
            'movies':movies,
            'movie_time':movie_time,
            'screens':screens,
            'seats':seats,
            'row':row
            }
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


