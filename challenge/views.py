from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect, Http404
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.


challenges = {
    "january": 'Start a daily gratitude journal to cultivate a positive mindset',
    "february": 'Take up a new hobby or learn a musical instrument',
    "march": 'Begin a fitness challenge or join a local sports team',
    "april": 'Explore new recipes and try your hand at cooking or baking',
    "may": 'Start a garden or create a mini herb garden on your windowsill',
    "june": 'Take up photography and capture the beauty of nature around you',
    "july": 'Plan a weekend getaway or a road trip to explore new places',
    "august": 'Volunteer for a cause or organization that you are passionate about',
    "september": 'Set aside time for self-care activities like meditation or yoga',
    "october": 'Get creative with DIY crafts or decorations for Halloween',
    "november": 'Start a novel writing challenge or participate in National Novel Writing Month (NaNoWriMo',
    "december": None,
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
        # return HttpResponseNotFound('<h2>This month is not supported</h2>')

        # response_data = render_to_string('404.html')
        # return HttpResponseNotFound(response_data)
        raise Http404()


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
