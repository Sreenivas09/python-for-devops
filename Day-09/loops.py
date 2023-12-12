for i in range(10):
    print(i)

students = ["Jhon", "Tip", "Snow", "Rest"]
for student in students:
    print(student)

number = 6
while number < 7:
    print(number)
    number += 1

list = [1, 2, 3, 4, 5, 6, 7, 8]
for line in list:
    if line == 3:
        break
    print(line) 

list = [1, 2, 3, 4, 5, 6, 7, 8]
for line in list:
    if line == 3:
        continue
    print(line)    
