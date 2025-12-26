from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie, Seat, Booking

def index(request):
    movies = Movie.objects.all()
    return render(request, 'cinema/index.html', {'movies': movies})


def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    return render(request, 'cinema/detail.html', {'movie': movie})


def seats(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.all()

    if request.method == 'POST':
        seat = Seat.objects.get(id=request.POST['seat'])
        seat.is_booked = True
        seat.save()
        Booking.objects.create(movie=movie, seat=seat, paid=True)
        return redirect('payment')

    return render(request, 'cinema/seats.html', {
        'movie': movie,
        'seats': seats
    })
def payment(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, 'cinema/payment.html', {'movie': movie})