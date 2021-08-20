import math
t = int(input())
while t > 0:
    l = []
    s1 = input()
    s = ''
    for i in s1:
        if i != '=':
            s = s + i
    max = -99999
    sum = 0
    for i in range(0, len(s) - 1):
        if s[i] != '=':
            sum = sum + 1
            if s[i] != s[i + 1]:
                if sum > max:
                    max = sum
                sum = 0
    if len(s) > 1 and s[i] != '=':
        if sum + 1 > max:
            max = sum + 1
    if len(s) == 1 and s[0] != '=':
        max = 1
    if max == -99999:
        print(1)
    else:
        print(max + 1)
    t = t - 1
