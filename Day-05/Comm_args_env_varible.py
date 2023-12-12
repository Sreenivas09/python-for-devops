import os
import sys

def add(a, b):
    a = a + b
    return a

def mul(a, b):
    m = a * b
    return m

def sub(a, b):
    s = a - b
    return s

a = float(sys.argv[1])
operation = sys.argv[2]
b = float(sys.argv[3])

if operation == "add":
    output = add(a, b)
    print("Value of Addition -" + str(output))

print(os.getenv("DB_Password"))
