n, a, b = list(map(int, input().split()))
x = list(map(int, input().split()))
ans = 0
for i in range(1, n):
    # 町(i-1)から町iに行く方法を考えてみよう～～～
    toho = a * (x[i] - x[i - 1])
    tele = b
    ans += min(toho, tele)
print(ans)
