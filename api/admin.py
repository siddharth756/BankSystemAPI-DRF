from django.contrib import admin
from .models import *

# Register your models here.

class BankAdmin(admin.ModelAdmin):
    list_display = ['bank_name','branch']

class BranchAdmin(admin.ModelAdmin):
    list_display = ['branch_name','branch_address','branch_code']

class AccountAdmin(admin.ModelAdmin):
    list_display = ['customer','bank','branch','account_number','account_type','balance','created_at']

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customer_name','customer_phone','customer_address']

class DepositAdmin(admin.ModelAdmin):
    list_display = ['account','amount']

class WithdrawAdmin(admin.ModelAdmin):
    list_display = ['account','amount']


admin.site.register(Bank, BankAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Withdraw, WithdrawAdmin)
admin.site.register(Deposit, DepositAdmin)
