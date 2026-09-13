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
            "latest_transaction": 0,
            "latest_timestamp": 0,
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
                        line.replace("Transaction", "").strip()
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

        # analysis 1

        total_transactions = len(transactions)
        deposits = 0
        withdrawals = 0

        # analysis 2

        total_deposits = 0
        latest_timestamp = 0
        largest_transaction = 0

        # analysis 3

        latest_transaction = "None" 
        latest_timestamp = "None"

        for transaction in transactions:
              transaction_type = transaction["type"]
              amount = transactions["amount"]
            if transaction_type == "Deposit":
                deposits += 1
                total_deposits += amount
            elif transaction_type == "Withdraw":
                withdrawals += 1
                total_withdrawn += amount

              

    pass