<h1>Welcome to BankSystemAPI</h1>

`
Here, i used Django REST Framework to create banking system api.
`

<h3>Models :</h3> 

Below are models that i used in this project.

1. Bank
2. Branch
3. Customer
4. Account
5. Deposit
6. Withdraw 

<h3>To clone repository :</h3> 


write below command in bash to clone this repository: 

```
git clone https://github.com/siddharth756/BankSystemAPI-DRF.git
```


<h3>API endpoints :</h3> 


Below are the endpoints to send requests and receive responses. 

api app runs at ```http://127.0.0.1:8000/api/``` .

#### 1. For Banks

 ```http://127.0.0.1:8000/api/bank/``` - to view and create bank. <br>
 ```http://127.0.0.1:8000/api/bank_detail/<int:pk>/``` - to retrieve, update and delete bank.

#### 2. Branch

 ```http://127.0.0.1:8000/api/branch/``` - to view and create branch. <br>
 ```http://127.0.0.1:8000/api/branch_detail/<int:pk>/``` - to retrieve, update and delete branch.

#### 3. Customer

 ```http://127.0.0.1:8000/api/customers/``` - to list all customers. <br>
 ```http://127.0.0.1:8000/api/branch_detail/<int:pk>/``` - to retrieve, update and delete customer.

#### 4. Account

 ```http://127.0.0.1:8000/api/create_account/``` - to craete account. <br>
 ```http://127.0.0.1:8000/api/accounts/``` - to list all accounts. <br>
 ```http://127.0.0.1:8000/api/account_detail/<int:pk>/``` - to retrieve, update and delete account.

#### 5. Deposit

 ```http://127.0.0.1:8000/api/deposit/``` - to deposit balance to account. 

#### 6. Withdraw 

 ```http://127.0.0.1:8000/api/withdraw/``` - to withdraw balance from account. 

<br>

` Thank you... `
