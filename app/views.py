from django.shortcuts import render
def bus_ticket_view(request):
    # Static data to pass to the template, if needed
    context = {
        'title': 'Bus Tickets',
        'message': 'Welcome to the Bus Ticketing System'
    }
    return render(request, 'app/index.html', context)
