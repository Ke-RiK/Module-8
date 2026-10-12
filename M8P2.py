# Kirill Kaminskyi M8P2.py 10/8/2026

#process
first_number  = 1
second_number = 1

print(first_number)
print(second_number)

for x in range(18):
    next_number = first_number + second_number

    first_number = second_number
    second_number = next_number

#output
    print (next_number)