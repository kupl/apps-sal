t = int(input())

while(t):
    ll = []
    lb = []
    cl = 0
    cb = 0
    a, b = input().split()
    a = int(a)
    b = int(b)

    for i in range(1, a + 1, 2):
        ll.append(i)
        if sum(ll) > a:
            ll.remove(i)
            break
    for i in range(2, b + 1, 2):
        lb.append(i)
        if sum(lb) > b:
            lb.remove(i)
            break
    if len(ll) > len(lb):
        print("Limak")
    else:
        print("Bob")
    t = t - 1
