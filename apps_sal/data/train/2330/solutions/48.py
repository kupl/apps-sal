S = input()
N = len(S)

if S[-1] == '1' or S[0] == '0':
    print(-1)

else:
    for i in range(N - 1):
        if S[i] != S[N - 2 - i]:
            print(-1)
            break
    else:
        tmp = 1
        for i in range(N - 1):
            if S[i] == '1':
                print(tmp, i + 2)
                tmp = i + 2
            else:
                print(tmp, i + 2)
