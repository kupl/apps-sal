a, b, c = list(map(int, input().strip().split()))
n = int(input().strip())

cnt = 0
cifre = list(map(int, input().strip().split()))
for e in cifre:
    if b < e < c:
        cnt += 1
print(cnt)
