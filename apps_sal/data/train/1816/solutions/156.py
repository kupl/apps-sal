class Solution:

    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:

        def time(strt):
            (h, m) = strt.split(':')
            h = h[1:] if h[0] == '0' else h
            m = m[1:] if m[0] == '0' else m
            return int(h) * 60 + int(m)
        use = collections.defaultdict(lambda: collections.deque(maxlen=3))
        ans = set()
        for (n, t) in sorted([(n, t) for (n, t) in zip(keyName, keyTime)], key=lambda x: x[1]):
            use[n].append(t)
            if len(use[n]) == 3 and abs(time(use[n][-1]) - time(use[n][0])) <= 60:
                print(n, use[n])
                ans.add(n)
        return sorted(ans)
