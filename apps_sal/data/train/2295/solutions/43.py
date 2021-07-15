n = int(input())
ans = []
sum_a = 0
for i in range(n):
    a, b = list(map(int, input().split()))
    sum_a += a
    if a > b:
        ans.append(b)
if ans == []:
    min_ans = sum_a
else:
    min_ans = min(ans)
print((sum_a-min_ans))

