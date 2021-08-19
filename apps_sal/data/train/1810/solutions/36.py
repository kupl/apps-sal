class Solution:

    def getFolderNames(self, names: List[str]) -> List[str]:
        memo = defaultdict(int)
        res = []
        for n in names:
            if memo[n] > 0:
                while n + '(' + str(memo[n]) + ')' in memo:
                    memo[n] += 1
                name = n + '(' + str(memo[n]) + ')'
                res.append(name)
                memo[name] += 1
            else:
                res.append(n)
            memo[n] += 1
        return res
