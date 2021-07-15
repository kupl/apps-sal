3
import sys
input = lambda: sys.stdin.readline().strip()
for _ in range(int(input())):
    n = int(input())
    print(min(i - 1 + (n + i - 1) // i - 1 for i in range(1, int(n ** 0.5) + 10)))

