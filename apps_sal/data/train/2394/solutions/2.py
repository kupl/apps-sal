for _ in range(int(input())):
    n = int(input())
    s = input()
    bal = 0
    minbal = 0
    for i in range(n):
        if s[i] == ')':
            bal -= 1
        else:
            bal += 1
        minbal = min(minbal, bal)
    print(-minbal)
