account_balance = 1000

transaction_type = str(input("You have $" + str(account_balance) + " in your bank account. Would you like to make a withdrawal or deposit? "))

transaction_amount = str(input("Thank you.  How much would you like to " + str(transaction_type) + "? "))

if transaction_type == "withdrawal":
    new_balance = account_balance - int(transaction_amount)
    if new_balance > 0:
        print("Withdrawing $" + str(transaction_amount) + " from your account. Your new balance is $" + str(new_balance) + ".")
    else:
        print("You cannot have a negative balance!")
elif transaction_type == "deposit":
    new_balance = account_balance + int(transaction_amount)
    print("Depositing $" + str(transaction_amount) + " to your account. Your new balance is $" + str(new_balance) + ".")
else:
    print("Invalid transaction.")
    