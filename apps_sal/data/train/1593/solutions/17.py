# cook your dish here
t = int(input())
for i in range(t):
    s = 0
    n = int(input())
    l = [100, 50, 10, 5, 2, 1]
    k = n
    it = 0
    total = 0
    l1 = []
    while(sum(l1) != n):
        r = k // l[it]
        total = total + r
        if(r != 0):
            l1.append(r * l[it])
            k = k % l[it]
        it += 1
    print(total)
