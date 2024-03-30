from django import forms

class JuegosForm(forms.Form):
    nombre = forms.CharField(max_length=100, required=True)
    genero = forms.CharField(max_length=30, required=True)
    empresa = forms.CharField(max_length=30, required=True)
    cantidad = forms.IntegerField(required=True)

class ConsolaForm(forms.Form):
    nombre = forms.CharField(max_length=30)
    empresa = forms.CharField(max_length=40)
    cantidad = forms.IntegerField(required=True)
