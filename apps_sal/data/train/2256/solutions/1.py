import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
ANS = []

for i in range(1, n // 2 + 1):
    for j in range(1, m + 1):
        sys.stdout.write((str(i) + " " + str(j) + "\n"))
        sys.stdout.write((str(n - i + 1) + " " + str(m - j + 1) + "\n"))


if n % 2 == 1:
    for j in range(1, m // 2 + 1):
        sys.stdout.write((str(n // 2 + 1) + " " + str(j) + "\n"))
        sys.stdout.write((str(n // 2 + 1) + " " + str(m - j + 1) + "\n"))

    if m % 2 == 1:
        sys.stdout.write((str(n // 2 + 1) + " " + str(m // 2 + 1) + "\n"))
