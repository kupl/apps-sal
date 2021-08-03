class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        d = {}
        for i, s in enumerate(req_skills):
            d[s] = i

        p = []
        for s in people:
            c = 0
            for t in s:
                c |= 1 << d[t]
            p.append(c)
        # print(p)

        self.tar = 2**len(req_skills) - 1
        self.r_len = len(people)
        self.r = []

        def dfs(l, t, cur):
            # print(l, t, cur, self.r)
            if cur == self.tar and len(l) < self.r_len:
                self.r_len = len(l)
                self.r = l.copy()
                return
            elif len(l) >= self.r_len or t > len(req_skills):
                return
            if cur & (1 << t):
                dfs(l, t + 1, cur)
            for i, k in enumerate(p):
                if k & (1 << t) and not i in l:
                    tmp = cur
                    l.append(i)
                    cur |= k
                    dfs(l, t + 1, cur)
                    cur = tmp
                    l.pop()

        dfs([], 0, 0)

        return self.r
