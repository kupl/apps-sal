# cook your dish here
t = int(input())
for i in range(t):
    p1, p2, k = list(map(int, (input()).split()))
    a = p1 + p2
    if (a // k) % 2 == 0:
        print("CHEF")
    else:
        print("COOK")
