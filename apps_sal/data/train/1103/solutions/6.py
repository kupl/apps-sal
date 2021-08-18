import fractions


def repeat_factor(n):
    fs = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            q = n / i
            if q % i == 0:
                return i
    return 1


nprobs = int(input())
for i in range(nprobs):
    x = input()
    prob = list(map(int, input().split()))
    found = False
    prod = 1
    for i in prob:
        prod *= i
    x = repeat_factor(prod)
    print(x)
