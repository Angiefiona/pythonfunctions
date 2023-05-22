class Bank:
    Account_status = "Active"
   
#    attributes
    def __init__(self, account_status, account_type, date_of_account_opening):
        self.Account_status = account_status
        self.Accout_type = account_type
        self.date_of_account_opening = date_of_account_opening
#   methods/behaviours
    def check_status(self):
        return f"Hello, your bank account is {self.Account_status}"
    
    def deposit_money(self, amount):
        self.balance = +amount
        return f"you have recevied{amount} and your new balance is {self.balance}"

# >> from bank import Bank
# >>> bank1 = Bank(Account_status="Active")
# >>> bank1.check_status()
# 'Hello, your bank account is Active'
# >>> 
# methods  - withdraw, deposit, transaction
 
# from bank1 import Account
# a = Account(account_name="Emily")
# a.deposit(1000)
# a.withdraw(500)
# a.deposit(600)


class Account:
 
 
 def __init__(self, account_name):
            self.account_name = account_name
            self.balance = 0

 def deposit(self, amount):
                self.balance += amount
                return f"you have deposited {amount} your new balance is{self.balance}"
 
 def withdraw(self, amount):
                if self.balance <= amount:
                    self.balance -= amount
                    return f"you have withdrawn {amount} your new balance is {self.balance}"
                else:
                    return f"Your balance is {self.balance} you cannot withdraw {amount}"
 # >>> from bank1 import Account
# >>> a = Account(account_name ="Mumo")
# >>> a.deposit(1000)
# 'you have deposited 1000 your new balance is1000'
# >>> a.deposit(500)
# 'you have deposited 500 your new balance is1500'
# >>> a.withdraw(600)
# 'Your balance is 1500 you cannot withdraw 600'
# >>> a.deposit(600)
# 'you have deposited 600 your new balance is2100'
# >>> 

# Add attributes deposits and withdrawals in the init method which are empty lists by default and 
# another attribute loan_balance which is zero by default.
class Account:
 
 
 def __init__(self, account_name):
            self.account_name = account_name
            self.balance = 0

 def deposit(self, amount):
                self.balance += amount
                return f"you have deposited {amount} your new balance is{self.balance}"
 
 def withdraw(self, amount):
                if self.balance <= amount:
                    self.balance -= amount
                    return f"you have withdrawn {amount} your new balance is {self.balance}"
                else:
                    return f"Your balance is {self.balance} you cannot withdraw {amount}"

 def __init__(self, account_name, balance):
        
        self.account_name = account_name
        self.deposit = []
        self.withdrawal = []
        self.loan_balance = 0

# Add a method check_balance which returns the account’s balance

 def check_balance(self):
         balance = sum(self.deposit) - sum(self.withdrawal)
         return balance
         
# Update the deposit method to append each withdrawal transaction to the deposits list. 
# Each transaction should be in form of a dictionary like this  
# {
#    "amount": amount,
#    "narration": “deposit”
# }
 def deposit(self, amount):
         self.balance += amount
         transaction = {"amount": amount, "narration": "deposit"}
         self.deposit.append(transaction)
         
         # {
    #    "amount": amount,
    #    "narration": "deposit"
    # }

     # >>> from bank1 import Account
# >>> a = Account(account_name ="Mumo")
# >>> a.deposit(1000)
# 'you have deposited 1000 your new balance is1000'
# >>> a.deposit(500)
# 'you have deposited 500 your new balance is1500'
# >>> a.withdraw(600)
# 'Your balance is 1500 you cannot withdraw 600'
# >>> a.deposit(600)
# 'you have deposited 600 your new balance is2100'
# >>> 