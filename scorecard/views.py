from django.shortcuts import render
from .models import Match, Score
from django.http import HttpResponse
import json


# Create your views here.
def Match_list(request):
    try:
        g_1 = 0
        g_2 = 0
        match=Match.objects.order_by('-id')[:2][::-1]
        cm=match[0]
        nm=match[1]
        tm_1 = Score.objects.filter(match=cm).filter(team=cm.t1).all()
        tm_2 = Score.objects.filter(match=cm).filter(team=cm.t2).all()
        for t in tm_1:
            g_1 += t.goal
        for t in tm_2:
            g_2 += t.goal

    except:
        match = None
        cm=''
        nm=''
        tm_1= ''
        tm_2 = ''

    return render(request, 'home.html', {'cm':cm,'nm':nm, 'tm_1':tm_1, 'tm_2': tm_2, 'g_1': g_1, 'g_2': g_2})

def Results_list(request):
    try:
        g_1 = 0
        g_2 = 0
        match=Match.objects.order_by('-id')[2:]
        for m in match:
            tm_1= Score.objects.filter(match=m).filter(team=m.t1).all()
            tm_2= Score.objects.filter(match=m).filter(team=m.t2).all()
            for t in tm_1:
                g_1 += t.goal
            for t in tm_2:
                g_2 += t.goal
            m.s1 = g_1
            m.s2 = g_2
            g_1 = g_2 = 0

        curr=match[0]
    except:
        match = None
        curr = ''

    return render(request, 'results.html', {'match':match,'curr':curr})

def get_subcategoty(request):
    match = request.GET.get('match','')
    qs = list(Match.objects.filter(id=int(match)).values('t1', 't2'))
    return HttpResponse(json.dumps(qs), content_type="application/json")
