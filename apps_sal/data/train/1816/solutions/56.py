class Solution:

    def alertNames(self, l1: List[str], l2: List[str]) -> List[str]:
        d = {}
        for i in l1:
            d[i] = [-float('inf')]
        ans = set()
        l = [[l1[i], l2[i]] for i in range(len(l1))]
        l.sort(key=lambda x: x[1])
        for i in range(len(l1)):
            l1[i] = l[i][0]
            l2[i] = l[i][1]
        for i in range(len(l1)):
            curr = l2[i]
            curr = curr.split(':')
            curr = int(''.join(curr))
            d[l1[i]].append(curr)
        ans = []
        for i in d:
            for j in range(2, len(d[i])):
                if d[i][j] - d[i][j - 2] <= 100:
                    ans.append(i)
                    break
        return sorted(ans)
