from django.forms import ModelForm
from .models import Item
class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['item_name', 'customer', 'total_kist_months', 'advance_taken', 'total_amount', 'plan', 'total_recieved', 'total_pending', 'net_rate', 'qty', 'imei', 'amount_in_words']

    def __init__(self, *args, **kwargs):
            super(ItemForm, self).__init__(*args, **kwargs)
            for visible in self.visible_fields():
                visible.field.widget.attrs['class'] = 'form-control'
