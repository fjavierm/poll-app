from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import CreatePollForm
from .models import Poll


# Create your views here.
def home(request):
    context = {}
    polls = Poll.objects.all()
    context['polls'] = polls
    return render(request, 'home.html', context)


def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreatePollForm()
    context = {
        'form': form
    }

    return render(request, 'create.html', context)


def vote(request, poll_id):
    context = {}
    poll = Poll.objects.get(id=poll_id)
    if request.method == 'POST':
        option = request.POST['poll']
        if option == 'option1':
            poll.choice_1_count += 1
        elif option == 'option2':
            poll.choice_2_count += 1
        elif option == 'option3':
            poll.choice_3_count += 1
        else:
            return HttpResponse(400, 'Option not found')
        poll.save()
        return redirect('result', poll_id)
    context['poll'] = poll
    return render(request, 'vote.html', context)


def result(request, poll_id):
    context = {}
    poll = Poll.objects.get(id=poll_id)
    context['poll'] = poll
    return render(request, 'result.html', context)
