import sys


def func(number):
    for i in range(len(number) - 1):
        if int(number[i]) > int(number[i + 1]):
            cifra = int(number[i]) - 1
            stringa = number[:i] + str(cifra) + '9' * (len(number) - i - 1)
            return func(stringa)
    return number


t = int(input().strip())
for _ in range(t):
    number = input().strip()
    stringa = func(number)
    while stringa[0] == '0':
        stringa = stringa[1:]
    print(stringa)
