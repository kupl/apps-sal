def prime(n):
    m = int(n ** 0.5) + 1
    t = [1] * (n + 1)
    for i in range(3, m):
        if t[i]: t[i * i :: 2 * i] = [0] * ((n - i * i) // (2 * i) + 1)
    return [2] + [i for i in range(3, n + 1, 2) if t[i]]

def gcd(a, b):
    c = a % b
    return gcd(b, c) if c else b

p = prime(31650)
def g(n):
    m = int(n ** 0.5)
    for j in p:
        if n % j == 0: return True
        if j > m: return False

def f(n):
    a, b = n, n + 1
    while g(a): a -= 1
    while g(b): b += 1
    p, q = (b - 2) * a + 2 * (n - b + 1), 2 * a * b
    d = gcd(p, q)
    print(str(p // d) + '/' + str(q // d))

for i in range(int(input())): f(int(input()))

