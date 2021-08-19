# cook your dish here
for i in range(int(input())):
    n, s = map(int, input().split())
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    m = []
    n = []
    for i in range(len(l1)):
        if l2[i] == 0:
            m.append(l1[i])
        else:
            n.append(l1[i])
    if len(m) > 0 and len(n) > 0:
        if 100 - s >= (min(m) + min(n)):
            print("yes")
        else:
            print("no")
    else:
        print("no")
