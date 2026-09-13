""" 
######### Learning Signature ######### 
Programmed by: Sedlex Monton
Date Submitted: September 13, 2026
 
Program Description: This program reads all lines in the transaction file
Reflection: I learned about the FileNotFoundError in try except.
 
AI Usage
[ ] No AI Assistance – Completed independently without AI.
[ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
"""

def view_history():
    # TODO 2:
    # Try to open transactions.txt
    # in read mode.
    try:
        with open("transactions.txt", "r") as file:
            lines = file.readlines()
            return True
    except FileNotFoundError:
        return[]

    pass