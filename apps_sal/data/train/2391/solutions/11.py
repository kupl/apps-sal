import heapq
import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    q = []
    for i in range(n):
        heapq.heappush(q, arr[i])
    pos = 0
    cnt = 0
    ans = []
    while pos < n - 2:
        tmp = heapq.heappop(q)
        if arr[pos] == tmp:
            pos += 1
            continue
        else:
            tpos = pos + arr[pos:].index(tmp)
            while tpos - pos >= 2:
                cnt += 1
                tpos -= 2
                ans.append(tpos + 1)
                (arr[tpos], arr[tpos + 1], arr[tpos + 2]) = (arr[tpos + 2], arr[tpos], arr[tpos + 1])
            if tpos - pos == 1:
                cnt += 2
                tpos -= 1
                ans.append(tpos + 1)
                ans.append(tpos + 1)
                (arr[tpos], arr[tpos + 1], arr[tpos + 2]) = (arr[tpos + 1], arr[tpos + 2], arr[tpos])
            pos += 1
    if arr[n - 2] <= arr[n - 1]:
        print(cnt)
        print(*ans)
    else:
        ttpos = -1
        for i in range(n - 2, -1, -1):
            if arr[i] == arr[i + 1]:
                ttpos = i
                break
        if ttpos == -1:
            cnt += 1
            ans.append(n - 2)
            (arr[n - 3], arr[n - 2], arr[n - 1]) = (arr[n - 1], arr[n - 3], arr[n - 2])
            if arr[n - 3] <= arr[n - 2] <= arr[n - 1]:
                print(cnt)
                print(*ans)
            else:
                cnt += 1
                ans.append(n - 2)
                (arr[n - 3], arr[n - 2], arr[n - 1]) = (arr[n - 1], arr[n - 3], arr[n - 2])
                if arr[n - 3] <= arr[n - 2] <= arr[n - 1]:
                    print(cnt)
                    print(*ans)
                else:
                    print(-1)
        else:
            cnt += 2
            ans.append(ttpos + 1)
            ans.append(ttpos + 1)
            (arr[ttpos], arr[ttpos + 1], arr[ttpos + 2]) = (arr[ttpos + 1], arr[ttpos + 2], arr[ttpos])
            q = []
            for i in range(n):
                heapq.heappush(q, arr[i])
            pos = 0
            while pos < n - 2:
                tmp = heapq.heappop(q)
                if arr[pos] == tmp:
                    pos += 1
                    continue
                else:
                    tpos = pos + arr[pos:].index(tmp)
                    while tpos - pos >= 2:
                        cnt += 1
                        tpos -= 2
                        ans.append(tpos + 1)
                        (arr[tpos], arr[tpos + 1], arr[tpos + 2]) = (arr[tpos + 2], arr[tpos], arr[tpos + 1])
                    if tpos - pos == 1:
                        cnt += 2
                        tpos -= 1
                        ans.append(tpos + 1)
                        ans.append(tpos + 1)
                        (arr[tpos], arr[tpos + 1], arr[tpos + 2]) = (arr[tpos + 1], arr[tpos + 2], arr[tpos])
                    pos += 1
            print(cnt)
            print(*ans)
