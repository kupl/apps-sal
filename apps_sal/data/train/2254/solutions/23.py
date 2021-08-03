import sys
input = sys.stdin.readline

n, q = map(int, input().split())
l = [[] for _ in range(n)]
is_read = []
is_read_idx = 0
ans = 0
prev_t = 0

for _ in range(q):
    ty, v = map(int, input().split())

    if ty == 1:
        l[v - 1].append(is_read_idx)
        is_read_idx += 1
        is_read.append(False)
        ans += 1
    elif ty == 2:
        for idx in l[v - 1]:
            if not is_read[idx]:
                is_read[idx] = True
                ans -= 1

        l[v - 1] = []
    else:
        if v > prev_t:
            for idx in range(prev_t, v):
                if not is_read[idx]:
                    is_read[idx] = True
                    ans -= 1

            prev_t = v

    print(ans)
