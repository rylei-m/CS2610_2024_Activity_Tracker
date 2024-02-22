import datetime
from django.shortcuts import render, redirect
from .models import Activity, TimeLog
from .forms import ActivityForm, TimeLogForm
from django.utils import timezone


def index(request):
    activities = Activity.objects.all()
    return render(request, 'RMactivitytracker/index.html', {'activities': activities})

def new_activity(request):
    if request.method == "POST":
        form = ActivityForm(request.POST)
        if form.is_valid():
            activity = form.save()
            return redirect('activity_detail', id=activity.id)
    else:
        form = ActivityForm()
    return render(request, 'RMactivitytracker/new_activity.html', {'form': form})

def activity_detail(request, id):
    activity = Activity.objects.get(id=id)
    timelogs = activity.timelog_set.all()
    return render(request, 'RMactivitytracker/activity_detail.html', {'activity': activity, 'timelogs': timelogs})


def new_timelog(request, activity_id):
    activity = Activity.objects.get(pk=activity_id)
    if request.method == 'POST':
        form = TimeLogForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            start_time = form.cleaned_data['start_time']
            end_time = form.cleaned_data['end_time']

            start_datetime = timezone.make_aware(datetime.datetime.combine(date, start_time))
            end_datetime = timezone.make_aware(datetime.datetime.combine(date, end_time))

            TimeLog.objects.create(activity=activity, start_time=start_datetime, end_time=end_datetime)

            return redirect('activity_detail', id=activity.id)
    else:
        form = TimeLogForm()
    return render(request, 'RMactivitytracker/new_timelog.html', {'form': form, 'activity': activity})