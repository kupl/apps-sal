# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    j = 1
    r = []
    b = a[0]
    while j < len(a):
        b = b % a[j]
        r.append(b)
        j += 1
    print(min(r))
