# cook your dish here
t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(i) for i in input().split()]
    min_val = 1000000
    for ele in arr:
        if min_val > ele:
            min_val = ele
    tot = 0
    for ele in arr:
        if ele != min_val:
            tot += ele
    print(min_val * tot)
