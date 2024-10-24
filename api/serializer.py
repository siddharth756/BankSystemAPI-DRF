from rest_framework import serializers
from .models import *


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = '__all__'

class BankSerializer(serializers.ModelSerializer):
    branch = BranchSerializer()

    class Meta:
        model = Bank
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class AccountSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    bank = BankSerializer()

    class Meta:
        model = Account
        fields = ['client','bank','open_date','account_type','balance']

class AccountDetailSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    bank = BankSerializer()
    balance = serializers.DecimalField(max_digits=12,decimal_places=2)

    class Meta:
        model = Account
        fields = ['client','bank','open_date','account_type','balance']

class TransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transfer
        fields = ['account','from_branch','to_branch','transfer_date']

    def validate(self, data):
        print(data)
        if data['account'].bank.branch == data['to_branch']:
            raise serializers.ValidationError("The account is already in this branch.")
        return data

    def create(self, validated_data):
        account = validated_data['account']
        print(account)
        account.bank.branch = validated_data['to_branch']
        account.save()

        transfer = Transfer.objects.create(**validated_data)
        return transfer

class WithdrawSerializer(serializers.ModelSerializer):
    class Meta:
        model = Withdraw
        fields = '__all__'

class DepositSerializer(serializers.ModelSerializer):
    class Meta:
        model = Deposit
        fields = '__all__'