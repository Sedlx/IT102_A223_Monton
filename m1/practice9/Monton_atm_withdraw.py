""" 
######### Learning Signature ######### 
Programmed by: Sedlex Monton
Date Submitted: September 13, 2026
 
Program Description: This program checks if the amount is valid, prints the withdrawal details and returns true of successful.
Reflection: I learned calling the account object and getting a boolean in return.
 
AI Usage
[ ] No AI Assistance – Completed independently without AI.
[ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
"""
from datetime import datetime

def withdraw_money(account, amount):
    # TODO 3:
    # Reject zero or negative withdrawal amounts.
    if amount <= 0:
        return False
 
    # TODO 4:
    # Call the Account object's withdraw()
    # method.
    success = amount.withdraw(amount)
 
    # TODO 5:
    # If successful, create a timestamp.
    if success:
        timestamp = datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
        with open("transactions.txt", "a") as file:
            file.write(f"Timestamp: {timestamp}\n")
            file.write(f"Account: {account.account_name}\n")
            file.write(f"Transaction: Withdraw\n")
            file.write(f"Amount: PHP {amount:.2f}\n\n")
        return True
    return False

    pass