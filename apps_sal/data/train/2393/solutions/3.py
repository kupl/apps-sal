T = int(input())

for t in range(T):
    N = int(input())
    M = []
    for i in range(N):
        row = input()
        M.append(row)

    for i in range(len(M) - 1):
        for j in range(len(M[i]) - 1):
            if M[i][j] == '1' and M[i + 1][j] == '0' and M[i][j + 1] == '0':
                print('NO')
                break
        else:
            continue
        break
    else:
        print('YES')
