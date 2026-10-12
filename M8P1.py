# Kirill Kaminskyi M8P1.py 10/6/2026

#input
principal_amount = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the interest rate: "))

#output
print(f"{"Year":<8} {"Beginning Balance":<20} {"Ending Balance":<20}")

#process

total_interest = 0
year = 1
while year <= 5:
    annual_interest = principal_amount * interest_rate
    ending_balance = principal_amount + annual_interest

    new_principal_amount = ending_balance


    total_interest = total_interest + annual_interest

#output

    print(f"{year:<8} ${principal_amount:<20,.2f} ${ending_balance:<20,.2f}")

#process
    year += 1
    principal_amount = new_principal_amount

#output

print(f"Total interest: ${total_interest:,.2f}")



