from django.db import models

# Create your models here.
class Tasks(models.Model):
    STATUS_CHOICES =[
        (1, 'A FAZER'),
        (2, 'FAZENDO'),
        (3, 'CONCLUIDO')
    ]
    status = models.IntegerField(choices=STATUS_CHOICES)

    def get_status_display(self):
        return dict(self.STATUS_CHOICES)[self.status]

    title = models.CharField(max_length=80, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    data = models.DateField(null=False, blank=False)
    status = models.IntegerField(choices=STATUS_CHOICES, null=False, blank=False)


