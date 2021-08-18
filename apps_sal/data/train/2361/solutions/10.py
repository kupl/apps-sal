import heapq


def solve(k):

    stack = [(-k, 0, k - 1)]
    heapq.heapify(stack)

    res = ["x" for _ in range(k)]
    cnt = 0

    while stack:
        cnt += 1
        length, start, end = heapq.heappop(stack)
        length = -length
        if length % 2 == 1:
            mid_point = (start + end) // 2
            res[mid_point] = cnt
            if not start == end:
                heapq.heappush(stack, (-(mid_point - start), start, mid_point - 1))
                heapq.heappush(stack, (-(mid_point - start), mid_point + 1, end))
        else:
            mid_point = (start + end - 1) // 2
            res[mid_point] = cnt
            if length == 2:
                heapq.heappush(stack, (-1, end, end))
            else:
                heapq.heappush(stack, (-(length // 2 - 1), start, mid_point - 1))
                heapq.heappush(stack, (-(length // 2), mid_point + 1, end))

    return " ".join([str(x) for x in res])


strr = input()
for _ in range(int(strr)):
    k = int(input())
    print(solve(k))
