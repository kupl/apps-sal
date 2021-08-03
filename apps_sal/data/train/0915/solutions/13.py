# cook your dish here
t = int(input())
i = 0
while i < t:
    n = int(input())
    a = []
    a = input().split()
    j = 0
    b = []
    fl = 0
    while j < n:
        x = int(a[j])
        if x not in b:
            c = a.count(a[j])
            if c > 1:
                fl = fl + c - 1
            b.append(x)
        j += 1
    fs = n - fl
    print(fs)
    i += 1
