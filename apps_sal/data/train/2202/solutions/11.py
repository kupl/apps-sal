def update(x, val):
    while x <= n:
        BIT[x] += val
        x += (x & -x)


def query(x):
    s = 0
    while x > 0:
        s = (s + BIT[x])
        x -= (x & -x)
    return s


n = int(input())
BIT = [0] * (n + 1)
for i in range(1, n + 1):
    update(i, i)
arr = list(map(int, input().split()))
answers = [0] * (n)
# print(BIT)
for i in range(n - 1, -1, -1):
    lol = arr[i]
    low = 0
    fjf = 0
    high = n
   # print(lol)
    while True:

        mid = (high + low + 1) // 2
        j = query(mid)
      #  print(mid,j)
      #  print(answers)
       # break
        if j > lol:
            if query(mid - 1) == lol:
                answers[i] = mid
                update(mid, -mid)
                break
            else:
                high = mid
        else:
            low = mid

print(*answers)
