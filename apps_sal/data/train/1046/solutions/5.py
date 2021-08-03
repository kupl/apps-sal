# cook your dish here
t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    l = 1
    m = 2
    flag = 0
    n = 3
    while l <= a and m <= b:
        if flag == 0:
            l = l + n
            flag = 1
            n = n + 1
        else:
            m = m + n
            flag = 0
            n = n + 1
    if l > a:
        print("Bob")
    else:
        print("Limak")
