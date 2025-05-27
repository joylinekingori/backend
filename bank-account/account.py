# Deposit: method to deposit funds, store the deposit and return a message with the new balance to the customer. It should only accept positive amounts.
class Account:
    def __init__(self,name):
        self.name=name
        self.deposits=[]
        self.withdrawals=[]
        self.balance=0 
        self.loan_amount=0
        self.accounts=[] 
        self.transactions=[]
        
    def deposit(self,amount):
        if amount>0:
            self.balance+= amount
            return(f"You have deposited KES {amount} your new balance is {self.balance}")

# Withdraw: method to withdraw funds, store the withdrawal and return a message with the new balance to the customer. An account cannot be overdrawn.
    def withdraw(self,amount):
        if amount>0:
            self.balance-= amount
            return(f"You have withdrawed KES {amount} your new balance is {self.balance}")



# Transfer Funds: Method to transfer funds from one account to an instance of another account.
    def transfer_funds(self,amount,target_account):
        self.withdrawals.append(amount)
        target_account.deposits.append(amount)
        self.balance-=amount
        return(f"You have transfereed KES {amount} your new balance is {self.balance}")



# Get Balance: Method to calculate an account balance from deposits and withdrawals.
    def get_balance(self,):
    
        return self.balance


# Request Loan: Method to request a loan amount.
    def request_loan(self, loan_amount):
        if loan_amount <= 0:
            return "Loan amount must be positive."
        self.balance += loan_amount
        self.loan_amount += loan_amount
        self.transactions.append(f"Requested loan of {loan_amount}")
        return f"Loan of {loan_amount} requested. New balance: {self.balance}"
#repay loan: Method to repay loan
    def repay_loan(self,amount):
        if amount > 0:
            self.loan_amount -= amount
            self.balance -= amount
            return f"You've repaid  {amount}, your remaining debt is {self.loan}"


# View Account Details: Method to display the account owner's details and current balance.
    def view_details(self):
        return f"Hello {self.name}. Your account balance is {self.balance} and you active loan status is {self.loan_amount} "


# Change Account Owner: Method to update the account owner's name.
    def change_owner(self,new_owner):
        self.new_owner=new_owner
        return f"New account holder is {new_owner}"
# Account Statement: Method to generate a statement of all transactions in an account. (Print using a for loop).
    def account_statement(self):
        # statement = f"Account Statement for Account #{self.account_number}"
        # statement += f"Initial Balance: {self.balance}"
        # statement += "Transactions"
        # for transaction in self.transactions:
        #     statement += f"- {transaction}"
        # statement += f"Final Balance: {self.balance}"
        # return statement


# Interest Calculation: Method to calculate and apply an interest to the balance. Use 5% interest. 
    def interest_calculate(self):
        interest=0.05
        answer= self.balance*interest 
        interested= answer+ self.balance
        
        return f"Interest of {interest} applied. Your new balance is {interested}"
# Freeze/Unfreeze Account: Methods to freeze and unfreeze the account for security reasons.
    def freeze_account(self):
        self.freeze=true
        return "Account frozen"
    def unfreeze_account(self):
        self.freeze=false
        return "Account unfrozen"

# Set Minimum Balance: Method to enforce a minimum balance requirement. You cannot withdraw if your balance is less than this amount.
    def set_min(self,minimum):
        self.minimum=minimum
        return f"Minimum balance set to {self.minimum}"
#Close Account: Method to close the account and set all balances to zero and empty all transactions.
    def close_account(self):
        self.active=active
        if self.active:
            self.balance=0
            self.active=false
            print(f"{self.name}'s account is closed")
        else:
            print("Account was closed")