n = int(input())
root = list(map(int, input().split()))
sums = list(map(int, input().split()))

direct = []
for i in range(n):
    direct.append([])
for i in range(n - 1):
    direct[root[i] - 1].append(i + 2)

# print(direct)

stack = [1]
s = sums[0]
work = True
while(len(stack) > 0 and work):
    v = stack.pop()
    # v is odd height
    for u in direct[v - 1]:
        if len(direct[u - 1]) == 0:
            sums[u - 1] = sums[v - 1]
        else:
            minval = -1
            for w in direct[u - 1]:
                if minval == -1 or minval > sums[w - 1]:
                    minval = sums[w - 1]
                s += sums[w - 1]
                stack.append(w)
            s -= minval * len(direct[u - 1])
            sums[u - 1] = minval
        if sums[u - 1] < sums[v - 1]:
            work = False
            break
        s += sums[u - 1] - sums[v - 1]

if work:
    print(s)
else:
    print(-1)
