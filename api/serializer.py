from rest_framework import serializers
from .models import *


class BranchSerializer(serializers.ModelSerializer):

    class Meta:
        model = Branch
        fields = '__all__'


class BankSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bank
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = '__all__'


class AccountSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['customer','bank','branch','account_number','account_type','balance','created_at']


class AccountDetailSerializer(serializers.ModelSerializer):
    balance = serializers.DecimalField(max_digits=12,decimal_places=2)

    class Meta:
        model = Account
        fields = ['customer','bank','branch','account_number','account_type','balance','created_at']


class WithdrawSerializer(serializers.ModelSerializer):

    class Meta:
        model = Withdraw
        fields = '__all__'


class DepositSerializer(serializers.ModelSerializer):

    class Meta:
        model = Deposit
        fields = '__all__'