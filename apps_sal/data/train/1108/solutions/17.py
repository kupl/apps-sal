inputs = list(map(int, input().split()))
n = inputs[0]
m = inputs[1]
k = inputs[2]
cnt = 0
for _ in range(0, n):
    arr = list(map(int, input().split()))
    ques = arr[len(arr) - 1]
    s = sum(arr) - ques
    if s < m:
        continue
    else:
        if ques <= 10:
            cnt = cnt + 1
print(cnt)
