t = int(input())
while t:
    t -= 1
    n = input()
    s = 0
    for i in n:
        s += int(i)
    if len(n) > 1 and s < 9:
        print(9 - (s % 9))
    else:
        print(min(s % 9, 9 - s % 9))
