import copy


class Solution:
    def countCharacters(self, w: List[str], c: str) -> int:

        d = {}

        for i in c:
            d[i] = d.get(i, 0) + 1
        ans = 0
        for i in range(len(w)):
            x = copy.deepcopy(d)
            f = True
            for j in w[i]:
                if j in x and x[j] > 0:
                    x[j] -= 1
                else:
                    f = False
                    break
            if f:
                ans += len(w[i])
        return ans
