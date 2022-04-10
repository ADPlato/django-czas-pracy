from django.forms import ModelForm
from .models import WorkingTime


class WorkingReportForm(ModelForm):
    class Meta:
        model = WorkingTime
        fields = '__all__'
