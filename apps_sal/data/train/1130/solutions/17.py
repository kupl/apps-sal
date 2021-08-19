# cook your dish here
t = int(input())
for _ in range(t):
    l1 = []
    l2 = []
    n, d = map(int, input().split())
    l = list(map(int, input().split()))
    for i in l:
        if i >= 80 or i <= 9:
            l1.append(i)
        else:
            l2.append(i)
    k1 = len(l1) % d
    k2 = len(l2) % d
    k3 = len(l1) // d
    k4 = len(l2) // d
    if k1 == 0 and k2 == 0:
        print(k3 + k4)
    elif k1 == 0 and k2 != 0:
        print(k3 + k4 + 1)
    elif k1 != 0 and k2 == 0:
        print(k3 + k4 + 1)
    elif k1 != 0 and k2 != 0:
        print(k3 + k4 + 2)
