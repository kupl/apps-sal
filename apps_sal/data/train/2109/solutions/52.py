from math import sqrt
q = int(input())
for _ in range(q):
    a, b = map(int, input().split())
    t = a * b
    s = int(sqrt(t))
    an = 2 * s - 2
    if s * s == t:
        an -= 1
    if s * (s + 1) < t:
        an += 1
    if a == b:
        an += 1
    print(an)
