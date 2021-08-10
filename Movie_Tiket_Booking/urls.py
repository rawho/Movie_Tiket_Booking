from django.contrib import admin
from django.urls import path
from movie.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home,name="home"),
    path('admin_home', Admin_Home,name="admin_home"),
    path('add_movie', Add_Movie,name="add_movie"),
    path('view_booking', View_Booking,name="view_booking"),
    path('all_booking', All_Booking,name="all_booking"),
    path('delete_movie<int:pid>', delete_movie,name="delete_movie"),
    path('movie_detail<int:pid>', Movie_detail,name="movie_detail"),
    path('book_ticket<int:pid>', Book_Ticket,name="book_ticket"),
    path('delete_booking<int:pid>', delete_booking,name="delete_booking"),
    path('delete_booking1<int:pid>', delete_booking1,name="delete_booking1"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
