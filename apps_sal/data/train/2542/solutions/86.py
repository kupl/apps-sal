class Solution:

    def isMonotonic(self, A: List[int]) -> bool:
        increase = []
        decrease = []
        (i, d) = ([], [])
        for (idx, v) in enumerate(A):
            while decrease and decrease[-1][0] >= v:
                (dv, di) = decrease.pop()
                if not d:
                    d.append((dv, di))
                elif d[-1][1] < di:
                    d.append((dv, di))
            decrease.append((v, idx))
            while increase and increase[-1][0] <= v:
                (iv, ii) = increase.pop()
                if not i:
                    i.append((iv, ii))
                elif i[-1][1] < ii:
                    i.append((iv, ii))
            increase.append((v, idx))
        if decrease and len(decrease) == 1:
            g = decrease.pop()
            if d and d[-1][0] >= g[0]:
                d.append(g)
            else:
                d.append(g)
        if increase and len(increase) == 1:
            g = increase.pop()
            if i and i[-1][0] <= g[0]:
                i.append(g)
            else:
                i.append(g)
        return len(i) == len(A) or len(d) == len(A)
