for _ in range(int(input())):
    n, z1, z2 = [int(i) for i in input().split()]
    A = [int(i) for i in input().split()]
    t1 = [i for i in A] + [-i for i in A]
    if z1 in t1 or z2 in t1:
        print(1)
    else:
        t2 = 2
        for val in t1:
            t3 = [val + t for t in t1]
            if z1 not in t3 and z2 not in t3:
                t2 = 0
                break
        print(t2)
