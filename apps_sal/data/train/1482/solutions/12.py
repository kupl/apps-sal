from sys import stdin, stdout
from math import floor
ans = []
for _ in range(int(stdin.readline())):
    n = int(stdin.readline())
    ans.append(f"1 {'1' + '0' * floor(n / 2)}")
stdout.write('\n'.join(ans))
