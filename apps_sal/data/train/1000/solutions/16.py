# cook your dish here
t = int(input())
while t:
    n = int(input())
    arr = list(map(int, input().split()))
    m = 0
    for i in arr:
        k = n/i
        if k != int(k):
            k = int(k) + 1
        if k > m:
            m = k
    print(int(m))
    t -=  1
