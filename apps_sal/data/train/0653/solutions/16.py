n = int(input())
arr = list(map(int, input().split()))
arr.sort()

p = int(input())
pt = 0
maxx = [0]
i = 0
ct = 1
while ct <= n:
    # print(p,pt)
    if arr[i] <= p:
        pt += 1
        maxx.append(pt)
        p -= arr[i]
        i += 1
        ct += 1
    else:
        p += arr[-1]
        arr.remove(arr[-1])
        pt -= 1
        ct += 1
# print(arr)

print(max(maxx))
