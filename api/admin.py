from django.contrib import admin
from .models import Bank, Branch, Client, Account, Transfer, Withdraw, Deposit

# Register your models here.

class BankAdmin(admin.ModelAdmin):
    list_display = ['name','branch']

class BranchAdmin(admin.ModelAdmin):
    list_display = ['name','address','branch_code']

class AccountAdmin(admin.ModelAdmin):
    list_display = ['client','bank','branch_name','open_date','account_type','balance']

    def branch_name(self,obj):
        return obj.bank.branch.name
    branch_name.short_description = 'branch name'

class ClientAdmin(admin.ModelAdmin):
    list_display = ['name','address']

class DepositAdmin(admin.ModelAdmin):
    list_display = ['account','amount']

class WithdrawAdmin(admin.ModelAdmin):
    list_display = ['account','amount']


admin.site.register(Bank, BankAdmin)
admin.site.register(Branch, BranchAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Account, AccountAdmin)
admin.site.register(Transfer)
admin.site.register(Withdraw, WithdrawAdmin)
admin.site.register(Deposit, DepositAdmin)
