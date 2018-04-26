from django.shortcuts import render_to_response, get_object_or_404
from .models import BookInfo
# Create your views here.

def index(request):
    booklist = BookInfo.objects.all()
    content = {}
    content['booklist'] = booklist
    return render_to_response('index.html', content)

def Herocontent(request, hero_id):
    hero = get_object_or_404(BookInfo, pk=hero_id)
    herolist = hero.heroinfo_set.filter(is_deleted=False)
    content = {}
    content['herolist'] = herolist
    return render_to_response('herocontent.html', content)