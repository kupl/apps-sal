def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


for _ in range(int(input())):
    N, A, B, K = map(int, input().split())

    lcm = (A * B) // gcd(A, B)
    appy = (N // A) - (N // lcm)
    chef = (N // B) - (N // lcm)

    print("Win") if appy + chef >= K else print("Lose")
