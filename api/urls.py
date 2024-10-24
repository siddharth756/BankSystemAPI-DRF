from django.urls import path 
from .views import *

urlpatterns = [
    path('bank/',BankAPIView.as_view(),name="bank"),
    path("bank_detail/<int:pk>/",BanksAPIView.as_view(),name="bank_detail"),
    path('branch/',BranchAPIView.as_view(),name="branch"),
    path('branch_detail/<int:pk>/',BranchesAPIView.as_view(),name="branch_detail"),
    path('create_account/',CreateAccountAPIView.as_view(),name="create_account"),
    path('accounts/',AccountListAPIView.as_view(),name="accounts"),
    path('account/<int:pk>/',AccountDetailAPIView.as_view(),name="account_detail"),
    path('deposit/',DepostiAPIView.as_view(),name="deposit"),
    path('withdraw/',WithdrawAPIView.as_view(),name="withdraw"),
    path('accounts/transfer_account/',AccountTransferAPIView.as_view(),name="transfer_account")
]
