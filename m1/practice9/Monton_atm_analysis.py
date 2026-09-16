""" 
######### Learning Signature ######### 
Programmed by: Sedlex Monton
Date Submitted: September 16, 2026
 
Program Description: This program processes each individual transaction an records it.
Reflection: I learned about timestamps and keeping track of relevant data.
 
AI Usage
[ ] No AI Assistance – Completed independently without AI.
[ ] AI as Support Tool – Used AI for explanations, syntax, or minor corrections.
[ ] AI as Collaborative Partner – Used AI to design, structure, or co-create significant code.
"""

def analyze_transactions():

    try:

        with open("transactions.txt", "r") as file:
            lines = file.readlines()

    except FileNotFoundError:

        return {
            "total_transactions": 0,
            "deposits": 0,
            "withdrawals": 0,
            "total_deposited": 0,
            "total_withdrawn": 0,
            "average_transaction": 0,
            "latest_transaction": "None",
            "latest_timestamp": "None",
            "largest_transaction": 0
        }

    transactions = []

    current = {}

    for line in lines:

        line = line.strip()

        if not line:
            continue

        if line.startswith("Timestamp:"):

            current["timestamp"] = (
                line.replace("Timestamp:", "").strip()
            )

        elif line.startswith("Account:"):

            current["account"] = (
                line.replace("Account:", "").strip()
            )

        elif line.startswith("Transaction:"):

            current["type"] = (
                line.replace("Transaction:", "").strip()
            )

        elif line.startswith("Amount:"):

            amount_text = (
                line.replace("Amount: PHP", "")
                .replace(",", "")
                .strip()
            )

            try:
                current["amount"] = float(amount_text)

            except ValueError:
                current["amount"] = 0.0

            
            if "type" in current and "amount" in current:

                transactions.append(current.copy())

            current = {}


  
    # ANALYSIS 1


    total_transactions = len(transactions)

    deposits = 0
    withdrawals = 0


 
    # ANALYSIS 2


    total_deposited = 0
    total_withdrawn = 0
    largest_transaction = 0



    # ANALYSIS 3

    latest_transaction = "None"
    latest_timestamp = "None"


    for transaction in transactions:

        transaction_type = transaction["type"]
        amount = transaction["amount"]

        # Count deposits
        if transaction_type == "Deposit":

            deposits += 1
            total_deposited += amount

        # Count withdrawals
        elif transaction_type == "Withdraw":

            withdrawals += 1
            total_withdrawn += amount


        # Find largest transaction
        if amount > largest_transaction:

            largest_transaction = amount


        # Get latest transaction
        latest_transaction = transaction_type

        
        if "timestamp" in transaction:

            latest_timestamp = transaction["timestamp"]


    

    if total_transactions > 0:

        total_amount = (
            total_deposited +
            total_withdrawn
        )

        average_transaction = (
            total_amount / total_transactions
        )

    else:

        average_transaction = 0


    return {
        "total_transactions": total_transactions,
        "deposits": deposits,
        "withdrawals": withdrawals,
        "total_deposited": total_deposited,
        "total_withdrawn": total_withdrawn,
        "average_transaction": average_transaction,
        "latest_transaction": latest_transaction,
        "latest_timestamp": latest_timestamp,
        "largest_transaction": largest_transaction
    }
    pass