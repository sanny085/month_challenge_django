from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.


challenges = {
    "january": '1 Do not eat meat',
    "february": '2 Every day please walk 20 mins',
    "march": '3 Exercie is very important for us',
    "april": '4 Do not eat meat',
    "may": '5 Every day please walk 20 mins',
    "june": '6 Exercie is very important for us',
    "july": '7 Do not eat meat',
    "august": '8 Every day please walk 20 mins',
    "september": '9 Exercie is very important for us',
    "october": '10 Do not eat meat',
    "november": '11 Every day please walk 20 mins',
    "december": '12 Exercie is very important for us',
}


def monthly_challenges(request, month):
    print('Monthly challenge, ', month)
    try:
        # challenge_text = f"<h1>{challenges[month]}</h1>"
        # challenge_text = render_to_string('challenge/challenge.html')
        # return HttpResponse(challenges[month])
        return render(request, 'challenge/challenge.html', {
            'month_name': month,
            'description': challenges[month],
            'value': 40,
        })
    except:
        return HttpResponseNotFound('<h2>This month is not supported</h2>')


def monthly_challenges_by_number(request, month):
    all_month = list(challenges.keys())
    if month > len(all_month):
        return HttpResponseNotFound('Invalid Month')

    challenge_text = all_month[month - 1]
    redirect_path = reverse('month_challenge', args=[challenge_text])
    return HttpResponseRedirect(redirect_path)


def display_tabular_month(request):
    all_month = list(challenges.keys())
    # listData = ''
    # for month in all_month:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse('month_challenge', args=[month])
    #     # Escape the "" (Double Quorts) through backslash
    #     listData += f"<li><a href=\"{month_path}\">{capitalized_month}</a></li>"

    # complete_month = f"<ul>{listData}</ul>"
    # return HttpResponse(complete_month)

    return render(request, 'challenge/index.html', {
        'all_month': all_month
    })
