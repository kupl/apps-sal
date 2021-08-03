res = []
for _ in range(int(input())):
    a, b = list(map(str, input().split()))
    res.append([a, int(b)])
res.sort(key=lambda x: x[-1])
# print(res)
for _ in range(int(input())):
    check = input().strip()
    f = 1
    for i in range(len(res) - 1, -1, -1):
        if res[i][0][:len(check)] == check:
            f = 0
            ans = res[i][0]
            break
    if f == 1:
        print("NO")
    elif f == 0:
        print(ans)
