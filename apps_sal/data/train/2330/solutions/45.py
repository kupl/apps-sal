S = input()

if S[-1] == "1" or S[0] == "0":
    print(-1)
else:
    flag = True
    for i in range((len(S) - 1) // 2):
        if S[-i - 2] != S[i]:
            flag = False
            print(-1)
            break

    if flag:
        ans = []
        now = 1
        nxt = 2
        for i in range(len(S) // 2):
            ans.append((now, nxt))
            if S[i] == "1":
                now = nxt
                nxt += 1
            else:
                nxt += 1
        ans.append((now, nxt))
        for i in range(nxt + 1, len(S) + 1):
            ans.append((now, i))
        for a in ans:
            print(*a)
