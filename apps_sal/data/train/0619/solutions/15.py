# cook your dish here
t = int(input())
for i in range(t):
    l, m, k = map(int, input().split())
    a = l + m + 1
    if a % k == 0:
        b = a / k
    else:
        b = int(a / k) + 1
    if b % 2 == 0:
        print("COOK")
    else:
        print("CHEF")
