# code chef may2012  chefluck.py


t = int(input())
for t1 in range(t):
    n = int(input())
    while n%7:
        n -= 4
    if n<0:
        print(-1)
    else:
        print(n)

