from sys import stdin

for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    n //= 2
    k = 2 * int(n**0.5)
    print(k)
