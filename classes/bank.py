class Bank:
    Account_status = "Active"
   
   
    def __init__(self, Account_status, Account_type, Date_of_account_opening):
        self.Account_status = Account_status
        self.Accout_type = Account_type
        self.Date_of_account_opening = Date_of_account_opening
  
    def check_status(self):
        return f"Hello, your bank account is {self.Account_status}"
