from collections import defaultdict

class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        memo = defaultdict(int)
        res = []
        for name in names:
            if memo[name] > 0:
                while f'{name}({memo[name]})' in memo.keys():
                    memo[name] += 1
                res.append(f'{name}({memo[name]})')
                memo[f'{name}({memo[name]})'] += 1
            else:
                res.append(name)
            memo[name] += 1
        return res
