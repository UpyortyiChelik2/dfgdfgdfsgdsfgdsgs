from .models import Booking
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['customer_name', 'customer_email'
            'start_time'
            'end_time', ]
        widgets = {'start_time': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
                   "end_time": forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
                   "customer_name": forms.TextInput(attrs={'class': 'form_control', 'placeholder': 'Ваше імя'}),
                   "customer_email": forms.EmailInput(attrs={'class': 'form_control', 'placeholder': 'pepe@gmail.com'})}
    def clean(self):
        cleaned_date = super().clean()
        start_time = cleaned_date.get('start_time')
        end_time = cleaned_date.get('end_time')
        room = self.initial.get('room') or cleaned_date.get('room')