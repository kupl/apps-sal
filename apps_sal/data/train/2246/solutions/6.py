import heapq
import sys
n, k = list(map(int, input().split()))
l = k
arr = list(map(int, input().split()))
add = int(input())
price = list(map(int, input().split()))
ans = 0
size = 0
s = [9999999999999999999]
heapq.heapify(s)
for i in range(n):
    heapq.heappush(s, price[i])
    size += 1
    if (arr[i] > l):
        # print(l)
        b = (arr[i] - l - 1) // add + 1
        if size < b:
            print(-1)
            return
        else:
            if b == 0:
                break
            for j in range(b):
                ans += heapq.heappop(s)
                l += add
                # print(ans)
                size -= 1
            # print("helo")
print(ans)
