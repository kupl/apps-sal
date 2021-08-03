t = int(input())
for i in range(t):
    n = input().split()
    if len(n) == 1:
        a = n[0]
        print(a.capitalize())
    else:
        for i in n:
            if i != n[-1]:
                a = i.capitalize()
                print(a[0], '.', sep='', end=' ')
            else:
                print(i.capitalize())
