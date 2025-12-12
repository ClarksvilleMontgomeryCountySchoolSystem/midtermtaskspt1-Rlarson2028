# Subtract withdrawal from balance
balance = starting_balance
balance -= withdrawal_amount

# Subtract ATM fee
balance -= atm_fee

# Calculate and subtract total monthly fees
total_monthly_fees = monthly_fee * months_inactive
balance -= total_monthly_fees

# Calculate full $20 bills and remaining dollars
full_twenties = balance // 20
remaining_dollars = balance % 20

# Display results with f-strings
print(f"Account Holder: {account_holder}")
print(f"Remaining Balance: ${balance}")
print(f"Full $20 Bills: {full_twenties}")
print(f"Remaining Dollars: ${remaining_dollars}")
