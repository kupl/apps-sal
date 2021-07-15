import sys
input = sys.stdin.readline
t = int(input())
s = [int(input()) for i in range(t)]
res = []
for num in s:
    num -= 1
    mod = num % 3
    num = num // 3
    div = 1
    while True:
        if num // div != 0:
            num -= div
            div *= 4
        else:
            break
    a = div + num
    b = a * 2
    tmp = a
    coff = 1
    while True:
        if tmp == 0:
            break
        if tmp % 4 == 2:
            b -= coff
        if tmp % 4 == 3:
            b -= coff * 5
        tmp = tmp // 4
        coff *= 4
    c = a ^ b
    if mod == 0:
        print(a)
    if mod == 1:
        print(b)
    if mod == 2:
        print(c)
