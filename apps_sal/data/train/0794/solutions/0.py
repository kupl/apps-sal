def multiple_input(): return map(int, input().split())


def list_input(): return list(map(int, input().split()))


mod = int(1e9) + 7
for _ in range(int(input())):
 n, m = multiple_input()
 a = list_input()
 a.sort()
 max_level = a[-1] + 1
 levels = [0] * max_level
 levels[0] = 1
 for i in a:
  levels[i] += 1
 ans = 1
 for i in range(1, max_level):
  ans = (ans * (pow(levels[i - 1], levels[i], mod))) % mod
 print(ans)
