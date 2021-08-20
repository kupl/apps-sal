for _ in range(int(input())):
    a = '0b' + input()
    b = '0b' + input()
    a = int(a, 2)
    b = int(b, 2)
    cnt = 0
    while b:
        U = a ^ b
        V = a & b
        a = U
        b = V * 2
        cnt += 1
    print(cnt)
