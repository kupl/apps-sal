for _ in range(int(input())):
 n, l, r = map(int, input().split(" "))
 ans_min = ((2 ** l) - 1) + (n - l)
 ans_max = ((2 ** r) - 1) + (n - r) * (2 ** (r - 1))
 print(ans_min, ans_max)
