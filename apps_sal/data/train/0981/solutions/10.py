def solve():
 input()
 s = sorted(map(int, input().split()))
 print(min(s[i + 1] - s[i] for i in range(len(s) - 1)))

for i in range(int(input())):
 solve()

