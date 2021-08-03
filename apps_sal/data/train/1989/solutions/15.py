class Solution:
    def longestAwesome(self, s: str) -> int:
        # alex wice solution
        P = [0]
        for c in s:
            x = int(c)
            P.append(P[-1])
            P[-1] ^= 1 << x

        dict = {}
        valid = {1 << x for x in range(10)}
        valid.add(0)
        ans = 0

        for j, q in enumerate(P):
            for target in valid:
                i = dict.get(q ^ target, None)
                if i is not None:
                    ans = max(ans, j - i)

                dict.setdefault(q, j)

        return(ans)
