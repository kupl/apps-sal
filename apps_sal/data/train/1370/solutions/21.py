for _ in range(int(input())):
    inp = [int(x) for x in input().split()]
    K = inp[0]
    N = inp[1]
    k1 = K % 10
    k2 = (K // 10) % 10
    k3 = (K // 100)
    if k1 == k2 == k3:
        print(1)
    elif k1 == k2 or k2 == k3 or k1 == k3:
        print(8)
    else:
        print(27)
