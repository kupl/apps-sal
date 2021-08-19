# cook your dish here
for i in range(int(input())):
    n, k = list(map(int, input().split()))
    remainder = (k - 2) % (n - 1)
    quotient = (k - 2) // (n - 1)
    k += remainder
    if (quotient % 2 == 1):
        feast = (1 + quotient) // 2
        print(((k % 1000000007) * (feast % 1000000007)) % 1000000007)
    else:
        feast = 1 + quotient
        k = k // 2
        print(((k % 1000000007) * (feast % 1000000007)) % 1000000007)
