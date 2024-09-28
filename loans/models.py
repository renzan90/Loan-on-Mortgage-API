from django.db import models
from datetime import datetime, date
from dateutil.relativedelta import relativedelta

class Loans(models.Model):
    
    loan_id = models.IntegerField(unique=True, primary_key=True)
    amount = models.DecimalField(max_digits=9, decimal_places=0)
    borrow_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=False, blank=False, \
                                   default=date.today()+relativedelta(years=1))
    income_eligibility = models.BooleanField(default=False)
    interest = models.DecimalField(max_digits=2, decimal_places=1)