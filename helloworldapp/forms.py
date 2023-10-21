# calculator/forms.py
from django import forms

class CalculatorForm(forms.Form):
    expression = forms.CharField(label='Enter an expression', max_length=200)
