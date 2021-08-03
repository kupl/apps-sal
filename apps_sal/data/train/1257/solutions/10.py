def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


t = int(input())
for c in range(t):
    n = int(input())
    print(factorial(n))
