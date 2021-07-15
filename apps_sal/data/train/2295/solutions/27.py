N = int(input())
sum_B = 0
min_B = 10**9 + 1
diff = False
for i in range(N):
  A, B = list(map(int, input().split()))
  if A != B:
    diff = True
  sum_B += B
  if A > B:
    min_B = min(B, min_B)
print((sum_B - min_B) if diff else 0)
