def I():
    return int(input())


def MI():
    return list(map(int, input().split()))


def LI():
    return list(map(int, input().split()))


'\ni=1は絶対ok．葉を繋ぐ辺を取れば良い\ni=NはNG．もともとN要素なので\nこれ，i=0の時ngという条件を足せば，左右対象ぽい．サイズがaとN-aができるため．\n\n「らしい」必要条件が分かった．必要十分だと嬉しい．\nO(N)に近い感じで解きたいので，順次構築していくイメージ．\n\n'


def main():
    mod = 10 ** 9 + 7
    S = input()
    N = len(S)
    if S[0] == '0' or S[-1] == '1':
        print(-1)
        return
    S = S[:-1]
    flag = 1
    for i in range(N - 1):
        if S[i] != S[-1 - i]:
            flag = 0
    if flag == 0:
        print(-1)
        return
    L = [(1, 2)]
    head = 2
    now = 3
    for s in S[1:]:
        L.append((head, now))
        if s == '1':
            head = now
        now += 1
    for a in L:
        print(' '.join(map(str, a)))


main()
