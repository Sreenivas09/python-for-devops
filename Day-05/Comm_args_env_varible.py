import os
import sys

def add():
    add = a + b
    return add

def mul():
    mul = a * b
    return mul

def sub():
    sub = a - b
    return sub

a = float(sys.argv[1])
operation = sys.argv[2]
b = float(sys.argv[3])

if operation == "add":
    output = add(a, b)
    print("Value of arguments -" + str(output))

print(os.getenv("DB_Password"))
