from collections import defaultdict
from bisect import bisect_left, bisect_right, insort_left, insort_right
import sys
input = sys.stdin.readline


def main():
    N = int(input())
    S = list(input())
    q = int(input())
    Q = [input() for _ in range(q)]

    dd = defaultdict(list)  # 各アルファベットが出現するインデックスをddに登録
    for i in range(ord('a'), ord('z') + 1):
        dd[chr(i)] = []
    for i, st in enumerate(S):
        dd[st].append(i)

    ans = []
    for q in Q:
        t, a, b = q.split()
        a = int(a) - 1
        if int(t) == 1:
            if S[a] == b:
                continue
            # 二分探索で該当するインデックスを取得
            id = bisect_left(dd[S[a]], a)
            dd[S[a]].pop(id)  # 取ってくる
            insort_left(dd[b], a)  # 新規に挿入する
            S[a] = b
        else:
            b = int(b) - 1
            cnt = 0
            for l in dd.values():
                # liの中身が存在し，
                # そのアルファベットの最後のインデックスが指定されている最初のindexよりも大きく．
                # a以上の最初のindexがb以下の時は，そのアルファベットの存在は保証される
                if l and a <= l[-1] and l[bisect_left(l, a)] <= b:
                    cnt += 1
            ans.append(cnt)
    print(*ans, sep='\n')


def __starting_point():
    main()


__starting_point()
