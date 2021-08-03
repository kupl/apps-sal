mod = 8589934592

for _ in range(int(input())):
    n = int(input())
    print("Case", (_ + 1), end="")
    print(": ", end="")
    print((pow(2, n, mod) - 1) % mod)
