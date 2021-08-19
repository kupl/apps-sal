alph = 'abcdefghijklmnopqrstuvwxyz'
t = int(input())
for _ in range(t):
    (n, m) = map(int, input().split())
    s = [input() for i in range(n)]
    for i in range(m):
        for char in alph:
            cand = s[0][0:i] + char + s[0][i + 1:]
            flag = False
            for j in range(n):
                cnt = 0
                for k in range(m):
                    if cand[k] != s[j][k]:
                        cnt += 1
                if cnt > 1:
                    flag = True
            if not flag:
                print(cand)
                break
        else:
            continue
        break
    else:
        print(-1)
