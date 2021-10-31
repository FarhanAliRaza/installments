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

# net_rate = models.Po
# qty = models.Positiv
# imei = models.CharFi
# amount_in_words = mo
#   item_name = models.CharField(max_length=255, blank=True, null=True)
#   customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
#   total_amount = models.PositiveIntegerField(null=True, blank=True)
#   total_recieved = models.PositiveIntegerField(null=True, blank=True)
#   total_pending = models.PositiveIntegerField(null=True, blank=True)
#   total_kist_months = models.CharField(max_length=3, default = '6', ch
#   advance_taken = models.PositiveIntegerField(null=True, blank=True)
#   plan = models.OneToOneField(Plan, on_delete= models.DO_NOTHING)
#   timestamp = models.DateTimeField(default=timezone.now)
#   def __str__(self):
# 

# class BuyerRegForm(forms.ModelForm):
    # class Meta:
        # model = Buyer
        # fields = ['location',]
        # widgets = {
            # 'location' : forms.TextInput(
                # attrs={
                    # "placeholder": "Business Name",
                    # "class": "form-control"
                # }),
        # }
        # labels = {
            # 'location ': _('location'),
        # }