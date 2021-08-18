
dic = {}
n, m = list(map(int, input().split()))
arr = list(range(1, n + 1))
sm = 0
for i in range(1, n + 1):
    sm += i
    dic[i] = 1

for i in range(m):
    el = int(input())
    if el in dic:
        arr[0], arr[-1] = arr[-1], arr[0]
        print(sm)

    else:
        prev = arr[-1]
        arr[-1] = el
        sm = sm - prev + el

        dic[el] = 1
        del dic[prev]

        print(sm)
