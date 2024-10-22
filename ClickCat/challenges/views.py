from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.

monthly_challenges = {
    "january":"Don't eat meat",
    "february":"Read a book every week",
    "march":"Walk 10,000 steps daily",
    "april":"No sugar for the whole month",
    "may":"Do 50 push-ups daily",
    "june":"Meditate for 15 minutes every day",
    "july":"Drink 2 liters of water daily",
    "august":"Practice a new hobby for 30 minutes daily",
    "september":"No social media after 8 PM",
    "november":"Write in a journal every day",
    "october":"Learn 10 new words daily",
    "december":"Spend 1 hour outside each day"
 

}


def index(request):
    months = list(monthly_challenges.keys())
    list_items = ""
 
    for month in months:
        month_path = reverse("month-challenge", args=[month])
        list_items += f"<li><a href=\"{month_path}\">{month}</a></li>"    
    response_data = f"<ul>{list_items}<ul>"
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound('Invalid Month')
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
    try:
        text = monthly_challenges[month]
        response_data = render_to_string("challenges/challenges.html")
        return HttpResponse(text)
    except:
        return HttpResponseNotFound("Month not recognized")  