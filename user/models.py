from django.db import models

class Borrower(models.Model):
    borrower_id = models.IntegerField(primary_key=True, unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=15, null=False, blank=False, default='')
    last_name = models.CharField(max_length=15, null=False, blank=False, default='')
    profession = models.CharField(max_length=15, null=False, blank=False, default='')
    email = models.EmailField()
    ph_no = models.CharField(max_length=10, unique=True)
    date_of_birth = models.DateField()

class BankDetails(models.Model):
    borrower = models.OneToOneField(Borrower, on_delete=models.CASCADE, primary_key=True)
    bank_name = models.CharField(max_length=25, null=False, blank=False)
    ifsc = models.CharField(max_length=25, null=False, blank=False)
    account_no = models.CharField(max_length=25, null=False, blank=False)
    upi_address = models.CharField(max_length=25, null=False, blank=False)

class KYC(models.Model):
    borrower = models.OneToOneField(Borrower, on_delete=models.CASCADE, primary_key=True)
    aadhar = models.CharField(max_length=25, null=False, blank=False)
    driving_license = models.FileField()
    utility_bill = models.FileField()
    pan = models.CharField(max_length=25, null=False, blank=False)

class IncomeDocs(models.Model):
    borrower = models.OneToOneField(Borrower, on_delete=models.CASCADE, primary_key=True)
    form16 = models.FileField()
    bank_statement1 = models.FileField()
    bank_statement2 = models.FileField()
    profession = models.CharField(max_length=25, null=False, blank=False)
    salary_slip = models.FileField()