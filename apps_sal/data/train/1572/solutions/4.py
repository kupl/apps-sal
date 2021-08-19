# cook your dish here
inputs = list(map(int, input().split()))
n = inputs[0]
A = inputs[1:n + 1]
P = inputs[n + 1:]
arr = [[] for _ in range(n)]

boss = None
for j, i in enumerate(P):
    if i == -1:
        boss = j
    else:
        arr[i - 1].append(j)


def BFS(array, start):
    queue = []
    queue.append(boss)
    maxi = -10000000000000000000000
    while queue:
        cur = queue.pop(0)
        val = A[cur]
        for i in arr[cur]:
            queue.append(i)
            cur_val = A[i]
            check = val - cur_val

            if check > maxi:
                maxi = check
            if val > cur_val:
                A[i] = val
    return maxi


if n == 1:
    print(0)
else:
    print(BFS(arr, boss))
