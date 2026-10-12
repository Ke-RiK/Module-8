# Kirill Kaminskyi M8P3.py 10/8/2026

#input
file = open("M8P3", "r")

total_bonus = 0

#process + output
print(f"{"Name:":<20} {"Salary:":20} {"Bonus:":<20}")

for x in range(6):
    name = file.readline().strip()
    salary = float(file.readline())
    empty_line = file.readline()

    if salary >= 100000.00:
        bonus_rate = 0.20
        bonus_amount = salary * bonus_rate
    elif salary >= 50000.00:
        bonus_rate = 0.15
        bonus_amount = salary * bonus_rate
    else:
        bonus_rate = 0.10
        bonus_amount = salary * bonus_rate

    total_bonus = total_bonus + bonus_amount

    print(f"{name:<20} ${salary:<15,.2f} ${bonus_amount:<15,.2f}")

#final output
print()
print(f"Total Bonus: ${total_bonus:,.2f}")