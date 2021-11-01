from django.db import models
from django.utils import timezone


class Customer(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    ref_name = models.CharField(max_length=200, blank=True, null=True)
    ref_phone = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    adress = models.CharField(max_length=255, blank=True, null=True)
    cnic = models.CharField(max_length=255, blank=True, null=True)


    def __str__(self):
        return self.name

mon_ch = (
    ('January', 'January'),
    ('February', 'February'),
    ('March'	, 'March'),
    ('April'	, 'April'),
    ('May', 'May'),
    ('June', 'June'),
    ('July', 'July'),
    ('August'	, 'August'),
    ('September', 'September'),
    ('October', 'October'),
    ('November', 'November'),
    ('December', 'December')
)



class Month(models.Model):
    name = models.CharField(max_length=200, choices = mon_ch,  default = 'none')
    year = models.PositiveIntegerField(null=True, blank=True)
    total = models.PositiveIntegerField(null=True, blank=True)
    recieved = models.PositiveIntegerField(null=True, blank=True)
    pending = models.PositiveIntegerField(null=True, blank=True)
    timestamp = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
class Plan(models.Model):
    months = models.ManyToManyField(Month, blank=True, null = True)


    def delete(self):
        if self.months:
            for i in self.months.all():
                i.delete()
        self.save()
        super(Plan, self).delete()

            

kist_choices = (
    ('6', '6'),
    ('10', '10'),


)
class Item(models.Model):
    item_name = models.CharField(max_length=255, blank=True, null=True)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, null=True, blank=True)
    total_amount = models.PositiveIntegerField(null=True, blank=True)
    total_recieved = models.PositiveIntegerField(null=True, blank=True)
    total_pending = models.PositiveIntegerField(null=True, blank=True)
    total_kist_months = models.CharField(max_length=3, default = '6', choices = kist_choices)
    advance_taken = models.PositiveIntegerField(null=True, blank=True)
    kist = models.PositiveIntegerField(null=True, blank=True)
    plan = models.OneToOneField(Plan, on_delete= models.DO_NOTHING, null=True, blank=True)
    timestamp = models.DateTimeField(default=timezone.now)
    net_rate = models.PositiveIntegerField(null=True, blank=True)
    qty = models.PositiveIntegerField(null=True, blank=True)
    imei = models.CharField(null=True, blank=True, max_length=255)
    amount_in_words = models.CharField(null=True, blank=True, max_length=255)


    def __str__(self):
        return    self.item_name + 'id ' + str(self.id)
    def delete(self):
        if self.customer:
            self.customer = None
            self.save()
        if self.plan:
            x = self.plan
            self.plan = None
            self.save()
            x.delete()

        super(Item, self).delete()








class Total(models.Model):
    total_rcvd = models.PositiveIntegerField(null=True, blank=True)
    total_pending = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return str(self.id)















# class Year(models.Model):













