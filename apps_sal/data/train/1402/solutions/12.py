for _ in range(int(input())):
    a = input()
    b = input()
    a, b = int(a, 2), int(b, 2)
    count = 0
    while b > 0:
        u = a ^ b
        v = a & b
        a = u
        b = v * 2
        count += 1
    print(count)
