# Kirill Kaminskyi M8P4.py 10/12/2026

#input
file = open("M8P5", "r")

total_tuition = 0
number_of_students = 0

#process + output
print(f"{"Last name:":<20} {"Credits taken:":<20} {"Tuition owned:":<20}")

for x in range(4):
    student_last_name = file.readline().strip()
    district_code = file.readline().strip()
    credits_taken = float(file.readline())
    empty_line = file.readline()

    if district_code == "I":
        cost_per_credit = 250
        tuition_owned  =  credits_taken * cost_per_credit

    elif district_code == "O":
        cost_per_credit = 500
        tuition_owned = credits_taken * cost_per_credit

    total_tuition += tuition_owned
    number_of_students += 1

    print(f"{student_last_name:<20} {credits_taken:<20} ${tuition_owned:<20,.2f}")

#final output
print()
print(f"Total tuition: ${total_tuition:,.2f}")
print()
print(f"Number of students: {number_of_students}")
