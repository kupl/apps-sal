import heapq
(n, initial) = list(map(int, input().split()))
target = list(map(int, input().split()))
gain = int(input())
prices = list(map(int, input().split()))
flag = True
for i in range(n):
    if target[i] > (i + 1) * gain + initial:
        flag = False
        print(-1)
        break
if flag:
    a = [10 ** 18]
    heapq.heapify(a)
    maxx = -1
    ans = 0
    for i in range(n):
        heapq.heappush(a, prices[i])
        if target[i] > initial:
            moves = (target[i] - initial - 1) // gain + 1
            if moves == 0:
                break
            else:
                for i in range(moves):
                    ans += heapq.heappop(a)
                    initial += gain
    print(ans)
