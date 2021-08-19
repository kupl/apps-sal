# cook your dish here
t = int(input())
for i in range(t):
    n = int(input())
    a = sorted(list(map(int, input().split())))
    b = a[0] % a[1]
    for n in a[2:]:
        b = b % n
    print(b)
