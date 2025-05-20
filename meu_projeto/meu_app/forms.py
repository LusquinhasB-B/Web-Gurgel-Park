from django import forms    

class EmailUpdateFormulario(forms.Form):
    novo_email = forms.EmailField(
        label='Novo Email',
        max_length=254,
        widget=forms.EmailInput(attrs={
            'placeholder': 'Digite seu novo email',
            'class': 'form-control'
        })
    )