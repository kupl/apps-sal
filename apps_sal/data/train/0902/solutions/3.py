t = int(input())
for _ in range(t):
    countDee = 0
    countDum = 0
    n, s = input().split(maxsplit=1)
    n = int(n)
    s = str(s)
    for i in range(n):
        b = str(input())
        if b[0] == '0':
            countDee += b.count('0')
        else:
            countDum += b.count('1')
    if countDee > countDum:
        print("Dee")
    elif countDee == countDum:
        if 'Dee' in s:
            print("Dum")
        else:
            print("Dee")
    else:
        print("Dum")
