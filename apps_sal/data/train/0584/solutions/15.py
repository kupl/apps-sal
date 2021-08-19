for N in range(int(input())):
    (count, nxt, prev) = (0, 0, 0)
    S = input()
    S = list(S)
    if S[0] == '1':
        for i in range(1, len(S)):
            if S[i] == '0' and nxt == 0 and (prev == 0):
                for j in range(i, len(S)):
                    if S[j] == '0':
                        count = count + 1
                    if j == len(S) - 1:
                        prev = prev + 1
                    elif S[j] == '1':
                        nxt = nxt + 1
                        break
            else:
                continue
    print(count)
