
from datetime import datetime
class Transaction:
    def __init__(self, amount, narration, transaction_type):
        self.date_time = datetime.now()
        self.amount = amount
        self.narration = narration
        self.transaction_type = transaction_type
    def view_details(self):
        return f"{self.date_time} | {self.transaction_type} | {self.narration} | Amount: {self.amount}"
class Account(Transaction):
    def __init__(self, owner, account_number):
        self.owner = owner
        self._account_number = account_number
        self._transactions = []
        self.balance = 0
        self._is_frozen = False
        self._loan = 0
        self.min_balance=20

    def account_number(self):
        return self.__account_number
    def deposit(self, amount):
        if self._is_frozen:

            return "Dear Customer your account is frozen.  Cannot deposit."
        if amount > 0:
            self.balance += amount
            self._transactions.append(f"Deposit: +KSH {amount}")
            return f"You have successfully deposited KSH {amount}.  Your current balance is: KSH {self.balance}.Thank you for banking with Equity Bank."
        else:
            return "Amount must be positive."
    def withdraw(self, amount):
        if self._is_frozen:
            return "Dear Customer your account is frozen.  Cannot deposit {amount}."
        if amount > 0:
            if self.balance - amount >= self.min_balance:
                self.balance -= amount
                self._transactions.append(f"Withdrawal: KSH {amount}")
                return f"You have successfully withdrawn KSH {amount} from your Equity bank account.Current balance is : KSH {self.balance}"
            else:
                return "Withdrawal request could not be processed. Insufficient funds."
        else:
            return "Invalid. Amount must be positive."
    def transfer_funds(self, target_acc,amount):
        if self._is_frozen:
            return "Dear Customer your account is frozen.  Cannot perform transfer."
        if amount > 0:
            if self.balance - amount >= self.min_balance:
                self.balance -= amount
                target_acc.deposit(amount)
                self._transactions.append(f"Transfer to {target_acc.account_number}: KSH{amount}")
                return f"You have transferred KSH {amount}."
            else:
                return "Transfer amount exceeds minimum balance."
        else:
            return "Invalid. Amount must be positive."
    def get_balance(self):
        return self.balance
    def request_loan(self, amount):
        if self._is_frozen:
            return "Account is frozen. Cannot request a loan."
        if amount > 0:
            self._loan += amount
            self._transactions.append(f"Loan Sent: KSH {amount}")
            return f"Loan of KSH{amount} approved. New balance: KSH {self.balance}, Loan balance: KSH {self._loan}"
        else:
            return "Invalid. Amount must be positive."
    def repay_loan(self, amount):
        if self._is_frozen:
            return "Account is frozen. Cannot repay loan."
        if amount > 0:
            if self._loan >= amount:
                self._loan -= amount
                self.balance -= amount
                self._transactions.append(f"Loan Repayment: KSH{amount}")
                return f"You have succesfully repaid KSH{amount}. Remaining balance is: KSH{self._loan}. New account balance: KSH{self.balance}"
            else:
                return "Repayment amount exceeds loan balance."
        else:
            return "Invalid repayment amount. Amount must be positive."
   
    def view_account_details(self):
            return f"Account Details: Account Number: {self._account_number}\n Account Holder: {self.owner}\n Current Balance: KSH{self.balance}\n Loan Balance: KSH{self._loan}"
        
    def change_account_owner(self, new_owner):
        self.owner = new_owner
        return f"Account owner updated to {new_owner}"
    def calculate_interest(self):
        interest_rate = 0.05
        interest = self.balance * interest_rate
        self.balance += interest
        self._transactions.append(f"Interest applied: KSH{interest:.2f}")
        return f"Interest of KSH{interest:.2f} applied. New balance: KSH{self.balance}"
    def freeze_account(self):
        if not self._is_frozen:
            self._is_frozen = True
            return "Your account has been frozen."
        else:
            return " Your account is already frozen."
    def unfreeze_account(self):
        if self._is_frozen:
            self._is_frozen = False
            return "Your account has been unfrozen."
        else:
            return "Your account is not frozen."
    def close_account(self):
        self.balance = 0
        self._loan = 0
        self._transactions = []
        return "Account closed. All balances set to zero and transactions cleared."
    
    