from django import forms
from signin.models import Orderlist



class OrderForm(forms.ModelForm):
    amount = forms.IntegerField(label='數量')
    
    class Meta:
        model = Orderlist
        fields = ['item', 'amount']