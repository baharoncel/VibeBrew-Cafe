from django import forms
from .models import Rezervasyon

class RezervasyonForm(forms.ModelForm):
    class Meta:
        model = Rezervasyon
        fields = ['isim', 'telefon', 'mesaj']
        widgets = {
            'isim': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 bg-slate-950 border border-slate-800 rounded-xl focus:outline-none focus:border-pink-500 text-sm text-white transition',
                'placeholder': 'Örn: Bahar',
                'required': 'required'
            }),
            'telefon': forms.TextInput(attrs={
                'class': 'w-full px-4 py-3 bg-slate-950 border border-slate-800 rounded-xl focus:outline-none focus:border-pink-500 text-sm text-white transition',
                'placeholder': '05XX XXX XX XX',
                'required': 'required'
            }),
            'mesaj': forms.Textarea(attrs={
                'class': 'w-full px-4 py-3 bg-slate-950 border border-slate-800 rounded-xl focus:outline-none focus:border-pink-500 text-sm text-white transition resize-none',
                'rows': 3,
                'placeholder': 'Kaç kişi geleceksiniz, özel bir isteğiniz var mı?',
                'required': 'required'
            }),
        }
