from typing import Iterable
from django.db import models

# Create your models here.

class Branch(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    branch_code = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Branches"

    def __str__(self):
        return self.name
    


class Bank(models.Model):
    name = models.CharField(max_length=255)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name 
    

class Client(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Account(models.Model):
    client = models.ForeignKey(Client,on_delete=models.CASCADE)
    open_date = models.CharField(max_length=255)
    account_type = models.CharField(max_length=255)
    bank = models.ForeignKey(Bank,on_delete=models.CASCADE)

    @property
    def balance(self):
        deposit = sum([deposit.amount for deposit in Deposit.objects.filter(account=self.id)])
        withdraw = sum([withdraw.amount for withdraw in Withdraw.objects.filter(account=self.id)])
        total = deposit - withdraw
        return total

    
    def __str__(self):
        return self.client.name    
    

class Transfer(models.Model):
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    from_branch = models.ForeignKey(Branch,on_delete=models.CASCADE,related_name="transfer_from")
    to_branch = models.ForeignKey(Branch,on_delete=models.CASCADE,related_name="transfer_to")
    transfer_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Transfer of {self.account.client.name} from {self.from_branch} to {self.to_branch}."

class Withdraw(models.Model):
    amount = models.FloatField()
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    

class Deposit(models.Model):
    amount = models.FloatField()
    account = models.ForeignKey(Account,on_delete=models.CASCADE)