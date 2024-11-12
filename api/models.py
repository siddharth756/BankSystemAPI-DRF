from django.db import models
import random

# Create your models here.

class Branch(models.Model):
    branch_name = models.CharField(max_length=255)
    branch_address = models.CharField(max_length=255)
    branch_code = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Branches"

    def __str__(self):
        return self.branch_name


class Bank(models.Model):
    bank_name = models.CharField(max_length=255)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.bank_name
    

class Customer(models.Model):
    customer_name = models.CharField(max_length=255)
    customer_address = models.CharField(max_length=255)
    customer_phone = models.CharField(max_length=15)

    def __str__(self):
        return self.customer_name
    

class Account(models.Model):
    bank = models.ForeignKey(Bank,on_delete=models.CASCADE)
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    account_number = models.CharField(max_length=12,unique=True,editable=False)
    account_type = models.CharField(max_length=25)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def balance(self):
        deposit = sum([deposit.amount for deposit in Deposit.objects.filter(account=self.id)])
        withdraw = sum([withdraw.amount for withdraw in Withdraw.objects.filter(account=self.id)])
        total = deposit - withdraw
        return total


    def save(self, *args, **kwargs):
        if not self.account_number:
            self.account_number = self.generate_account_number()
        
        super(Account, self).save(*args, **kwargs)

    def generate_account_number(self):
        while True:
            account_number = ''.join([str(random.randint(0, 9)) for _ in range(12)])
            if not Account.objects.filter(account_number=account_number).exists():
                return account_number


    def __str__(self):
        return self.customer.customer_name 

class Withdraw(models.Model):
    amount = models.FloatField()
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    

class Deposit(models.Model):
    amount = models.FloatField()
    account = models.ForeignKey(Account,on_delete=models.CASCADE)