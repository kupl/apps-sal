def main():
    import sys
    input = sys.stdin.readline
    for __ in [0]*int(input()):
        N = int(input())
        S = [tuple(map(int, input()[:-1])) for _ in [0]*N]

        for i in range(N-1):
            for j in range(N-1):
                if S[i][j] and S[i+1][j] == S[i][j+1] == 0:
                    print('NO')
                    break
            else:
                continue
            break
        else:
            print('YES')


def __starting_point():
    main()

__starting_point()
