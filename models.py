from django.db import models

class Activity(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def time_spent(self):
        from datetime import timedelta
        delta = timedelta()
        for timelog in self.timelog_set.all():
            delta += (timelog.end_time - timelog.start_time)
        return delta.total_seconds() / 3600

class TimeLog(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.activity.name} - {self.start_time} to {self.end_time}"
