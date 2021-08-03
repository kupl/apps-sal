import sys

for __ in range(eval(input())):
    a, b = input().lower(), input().lower()
    if a > b:
        print("second")
    elif a < b:
        print("first")
    else:
        print("equal")
