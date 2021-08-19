t = int(input())
for _ in range(t):
    K = int(input())
    K -= 1
    A = 2
    B = 10
    M = 10 ** 9 + 7
    while K > 0:
        if K % 2 != 0:
            B = B * A % M
            K -= 1
        else:
            A = A ** 2 % M
            K //= 2
    print(B)
