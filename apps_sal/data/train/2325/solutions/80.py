# 【考察】
# (1) A と B は入れ替え可能：
#   AB -> AAA -> BBAA -> BBBBA -> BA
# (2) AB と BA は空文字に置換可能：
#   AB -> AAA -> ''
# (3) 一つの文字から3つずつ同じ文字を増やしていくことが可能
#   A -> BB -> AAB -> AAAA
# 以上の点より、A・Bの個数の差のmod3の値が本質的だとわかる。


def cumsum_a(st):
    cs = [0] * len(st)
    for i, s in enumerate(st):
        if s == 'A':
            cs[i] = 1
        if i > 0:
            cs[i] += cs[i - 1]
    return cs


def main():
    S = input()
    T = input()
    Q = int(input())
    query_list = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(Q)]
    # Aの個数の累積和をとる（bはaの個数からわかる）
    s_cs_a, t_cs_a = cumsum_a(S), cumsum_a(T)
    for query in query_list:
        s_left, s_right, t_left, t_right = query
        s_count_a = s_cs_a[s_right]
        if s_left > 0:
            s_count_a -= s_cs_a[s_left - 1]
        s_count_b = s_right - s_left + 1 - s_count_a
        t_count_a = t_cs_a[t_right]
        if t_left > 0:
            t_count_a -= t_cs_a[t_left - 1]
        t_count_b = t_right - t_left + 1 - t_count_a
        # 個数の差のmod3の値で比較する
        s_diff = (s_count_a - s_count_b) % 3
        t_diff = (t_count_a - t_count_b) % 3
        if s_diff == t_diff:
            print('YES')
        else:
            print('NO')


def __starting_point():
    main()


__starting_point()
