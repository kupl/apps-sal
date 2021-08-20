class SortedList(list):

    def add(self, other):
        left = -1
        right = len(self)
        while right - left > 1:
            mid = right + left >> 1
            if other < self[mid]:
                right = mid
            else:
                left = mid
        super().insert(right, other)


INF = int(3e+18)


def solve_good(n, m, d, a, b, t):
    left = SortedList()
    left.append(-INF)
    right = SortedList()
    right.append(INF)
    lborder = -INF
    rborder = INF
    tprev = 0
    ans = 0
    for (ai, bi, ti) in zip(a, b, t):
        ans += bi
        dt = ti - tprev
        interval = dt * d
        tprev = ti
        lborder += interval
        rborder -= interval
        lefta = lborder + ai
        righta = rborder - (n - ai)
        if lefta < left[-1]:
            top = left.pop()
            ans -= abs(top - lefta)
            left.add(lefta)
            left.add(lefta)
            right.add(rborder - (n - abs(top - lborder)))
        elif righta > right[0]:
            top = right.pop(0)
            ans -= abs(top - righta)
            right.add(righta)
            right.add(righta)
            left.add(lborder + n - abs(top - rborder))
        else:
            left.add(lefta)
            right.add(righta)
    return ans


(n, m, d) = [int(elem) for elem in input().split()]
(a, b, t) = ([], [], [])
for i in range(m):
    (ai, bi, ti) = [int(elem) for elem in input().split()]
    a.append(ai)
    b.append(bi)
    t.append(ti)
print(solve_good(n, m, d, a, b, t))
