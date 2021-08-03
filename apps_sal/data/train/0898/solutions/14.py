# cook your dish here

for i in range(int(input())):
    m, n = map(int, input().split())

    if n < 9:
        y = 0
    elif n >= 9 and n < 99:
        y = 1
    elif n >= 99 and n < 999:
        y = 2
    elif n >= 999 and n < 9999:
        y = 3
    elif n >= 9999 and n < 99999:
        y = 4
    elif n >= 99999 and n < 999999:
        y = 5
    elif n >= 999999 and n < 9999999:
        y = 6
    elif n >= 9999999 and n < 99999999:
        y = 7
    elif n >= 99999999 and n < 999999999:
        y = 8
    elif n >= 999999999:
        y = 9
    print(m * y, m)
