class Solution:
    def getFolderNames(self, names: List[str]) -> List[str]:
        mem = collections.defaultdict(int)
        res = []
        for n in names:
            if mem[n] > 0:
                while n + '(' + str(mem[n]) + ')' in mem:
                    mem[n] += 1
                res.append(n + '(' + str(mem[n]) + ')')
                mem[n + '(' + str(mem[n]) + ')'] += 1
            else:
                res.append(n)
            mem[n] += 1
        return res
