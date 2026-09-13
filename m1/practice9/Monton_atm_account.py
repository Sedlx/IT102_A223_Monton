""" 
######### Learning Signature ######### 
Programmed by: Sedlex Monton
Date Submitted: September 13, 2026
 
Program Description: This program houses the Account Class and supports the account
name, balance, deposit withdraw and check balance function.
Reflection: I learned how to create a github repository to create a modular program.
 
AI Usage
[ ] No AI Assistance – Completed independently without AI.
[ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
"""
class Account:
 
    def __init__(self, name, starting_balance):
        # TODO 2:
        # Store the account name.
        self.account_name = name
        # TODO 3:
        # Store the starting balance as an internal attribute.
        self._balance = starting_balance

        pass
 
 
    # TODO 4:
    # Create check_balance().
    #
    # This method should return the current
    # account balance.
 
 
    def check_balance(self):
        return self._balance
        pass
 
 
    # TODO 5:
    # Create deposit().
    #
    # If amount is greater than zero:
    # - increase the balance
    # - return True
    #
    # Otherwise:
    # - return False
 
 
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            return True
        else:
            return False
        pass
 
 
    # TODO 6:
    # Create withdraw().
    #
    # The withdrawal should only be successful when:
    # - amount > 0
    # AND
    # - amount <= current balance
    #
    # If successful:
    # - decrease the balance
    # - return True
    #
    # Otherwise:
    # - do not change the balance
    # - return False
 
 
    def withdraw(self, amount):
        if amount > 0 and amount <= self._balance:
            self._balance -= amount
            return True
        else:
            return False
        pass