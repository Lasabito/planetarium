from django import forms

from Planetarium.web.models import NewRoomModel


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class NewRoomForm(forms.ModelForm):
    class Meta:
        model = NewRoomModel
        fields = ['number', 'heading', 'duration', 'date', 'time']
        labels = {
            'number': 'Номер на прожекция',
            'heading': 'Заглавие',
            'duration': 'Времетраене (мин)',
            'date': 'Дата',
            'time': 'Час',
        }
        widgets = {
            'date': DateInput(),
            'time': TimeInput(),
        }

