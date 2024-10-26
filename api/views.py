from django.shortcuts import render
from django.db import transaction
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import * 
from .serializer import *

# -------------- bank -------------

def HomeView(request):
    return render(request, 'home.html')

class BankAPIView(generics.ListCreateAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


class BanksAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bank.objects.all()
    serializer_class = BankSerializer


# -------------- branch -------------


class BranchAPIView(generics.ListCreateAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer 


class BranchesAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Branch.objects.all()
    serializer_class = BranchSerializer


# -------------- create customer -----------

class CustomerListAPIView(generics.ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# -------------- create account ----------

class CreateAccountAPIView(APIView):
    @transaction.atomic
    def post(self,request):
        customer = Customer.objects.create(
            customer_name = request.data['customer_name'],
            customer_address = request.data['customer_address'],
            customer_phone = request.data['customer_phone']
        )
        bank = Bank.objects.get(pk=request.data['bank'])
        branch = Branch.objects.get(pk=request.data['branch'])

        account = Account.objects.create(
            customer = customer,
            bank = bank,
            branch = branch,
            account_type = request.data['account_type'],
        )

        balance = request.data.get('balance',0)
        if balance > 0:
            Deposit.objects.create(account=account, amount=balance)

        serializer = AccountSerializer(account).data
        return Response(serializer,status=status.HTTP_201_CREATED)


# -------------- accounts ----------

class AccountListAPIView(generics.ListAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


# -------------- account_detail ----------

class AccountDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountDetailSerializer


# -------------- deposit ----------

class DepostiAPIView(generics.ListCreateAPIView):
    queryset = Deposit.objects.all()
    serializer_class = DepositSerializer


# -------------- withdraw ----------

class WithdrawAPIView(generics.ListCreateAPIView):
    queryset = Withdraw.objects.all()
    serializer_class = WithdrawSerializer
      