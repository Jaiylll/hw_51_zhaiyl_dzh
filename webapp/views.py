from django.shortcuts import render, HttpResponseRedirect

from webapp.models import Cat


# Create your views here.
def index(request):
    return render(request, 'index.html')


def add_cat(request):
    name = request.POST.get('name')
    cat = Cat(name=name)
    context = {'name': cat.name,
               'age': cat.age,
               'satiety': cat.satiety,
               'happiness': cat.happiness}
    return render(request, "about.html", context=context)


def cat_actions(request):
    name = request.POST.get('name')
    needed_cat = None
    for cat in Cat.cats:
        if cat.name == name:
            needed_cat = cat
    action = request.POST.get('action')
    if action == "feed":
        needed_cat.feed(needed_cat)
    elif action == "play":
        needed_cat.play(needed_cat)
    elif action == "sleep":
        needed_cat.put_to_sleep(needed_cat)
    else:
        pass
    context = {'name': needed_cat.name,
               'age': needed_cat.age,
               'satiety': needed_cat.satiety,
               'happiness': needed_cat.happiness,
               'is_asleep': needed_cat.is_asleep}
    return render(request, "about.html", context=context)
