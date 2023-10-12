from django import forms

class FormComentario(forms.Form):
    autor = forms.CharField(max_length=50, 
    widget=forms.TextInput(attrs={'class': 'form-control', 
    'placeholder' : 'Ingresa el nombre del autor'}))

    body = forms.CharField(
        widget=forms.Textarea(attrs={ 
            'class': 'form-control', 
            'placeholder' : 'Deja tu comentario aquí'
        })
    )