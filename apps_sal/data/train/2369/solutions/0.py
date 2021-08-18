
import sys


class GCandyBoxHardVersion:
    def solve(self):
        q = int(input())
        for _ in range(q):
            n = int(input())
            a = [0] * n
            f = [0] * n
            for i in range(n):
                a[i], f[i] = [int(_) for _ in input().split()]

            d = {key: [0, 0] for key in a}
            for i in range(n):
                d[a[i]][f[i]] += 1
            rev_d = {sum(key): [] for key in list(d.values())}
            for x in d:
                rev_d[d[x][0] + d[x][1]] += [d[x]]

            for x in rev_d:
                rev_d[x].sort(key=lambda item: item[1])

            cur = max(rev_d)
            cnt = max(rev_d)
            nb_candies = 0
            given_away = 0
            while 1:
                if cnt == 0 or cur == 0:
                    break
                if cur > cnt:
                    cur -= 1
                    continue

                if cnt not in rev_d or not rev_d[cnt]:
                    cnt -= 1
                    continue

                mx_f = -1
                v = -1
                for max_cnt in range(cur, cnt + 1):
                    if max_cnt in rev_d and rev_d[max_cnt] and rev_d[max_cnt][-1][1] > mx_f:
                        v = max_cnt
                        mx_f = rev_d[max_cnt][-1][1]
                to_take = rev_d[v].pop()
                nb_candies += cur
                given_away += min(to_take[1], cur)
                cur -= 1
            print(nb_candies, given_away)


solver = GCandyBoxHardVersion()
input = sys.stdin.readline

solver.solve()
