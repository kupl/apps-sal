t = int(input())
for _ in range(t):
    h, w, h_cnt, w_cnt = map(int, input().split())
    if h_cnt * h != w_cnt * w:
        print("NO")
        continue

    ans = [[0] * w for i in range(h)]    
    j = 0
    for i in range(h):
        cnt = h_cnt
        while cnt > 0:
            ans[i][j % w] = 1
            j += 1
            cnt -= 1
    print("YES")
    for res in ans:
        print("".join(map(str, res)))
