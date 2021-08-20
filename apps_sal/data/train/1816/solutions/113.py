class Solution:

    def alertNames(self, a: List[str], t: List[str]) -> List[str]:

        def alerted(a):
            for i in range(len(a) - 2):
                if a[i + 2] - a[i] <= 60:
                    return True
            return False
        d = defaultdict(list)
        for (name, t) in zip(a, t):
            (h, m) = map(int, t.split(':'))
            d[name].append(h * 60 + m)
        ans = []
        for name in d:
            d[name].sort()
            if alerted(d[name]):
                ans.append(name)
        return sorted(ans)
