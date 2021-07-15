class Solution:
    def peopleIndexes(self, fv: List[List[str]]) -> List[int]:
        
        dic = defaultdict(lambda : set())
        for i in range(len(fv)):
            for cmp in fv[i]:
                dic[cmp].add(i)
        ans = []
        ind = 0
        for lst in fv:
            st = None
            for cmp in lst:
                if st:
                    st &= dic[cmp]
                else:
                    st = dic[cmp].copy()
            if len(st) == 1:
                ans.append(ind)
            ind += 1
        return sorted(ans)

