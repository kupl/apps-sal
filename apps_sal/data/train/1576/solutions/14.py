for tc in range(int(input())):
    K = int(input())
    S = [str(i) for i in range(1, K + 1)]
    for i in range(K):
        print(''.join(S))
        S = S[1:] + [S[0]]
