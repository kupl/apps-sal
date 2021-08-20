from collections import defaultdict
import sys
import heapq


def input():
    return sys.stdin.readline()


def solution():
    n = int(input())
    candi = [[0, 0] for i in range(n + 1)]
    que = []
    for i in range(n):
        (taste, youwant) = list(map(int, input().split()))
        if youwant == 1:
            candi[taste][0] += 1
        else:
            candi[taste][1] += 1
    for i in range(n + 1):
        s = sum(candi[i])
        if s > 0:
            que.append((-s, -candi[i][0], -candi[i][1]))
    heapq.heapify(que)
    ans = 0
    badcnt = 0
    border = -que[0][0]
    stocked = []
    heapq.heapify(stocked)
    ording = 0
    while (que or stocked) and border > 0:
        ording += 1
        while que and que[0][0] <= -border:
            (poped_cnt, poped_good_candi, poped_bad_candi) = heapq.heappop(que)
            heapq.heappush(stocked, (poped_good_candi, poped_bad_candi))
        if not stocked:
            if que:
                border = -que[0][0]
            continue
        if stocked:
            (good_candi, bad_candi) = heapq.heappop(stocked)
            good_candi *= -1
            bad_candi *= -1
            sums = good_candi + bad_candi
            if sums < border:
                ans += sums
                border = sums - 1
                badcnt += good_candi
                continue
            elif sums >= border:
                ans += border
                badcnt += min(border, good_candi)
                border -= 1
                continue
    print(ans, badcnt)
    return


def main():
    test = int(input())
    for i in range(test):
        solution()
    return


def __starting_point():
    main()


__starting_point()
