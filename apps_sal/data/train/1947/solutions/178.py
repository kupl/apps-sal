class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        d = {}
        for i in B:
            temp = Counter(i)
            for j in temp:
                d[j] = max(d.get(j,0),temp[j])
        
        ans = []
        for i in A:
            temp = Counter(i)
            flag = True
            for j in d:
                if(temp.get(j) and temp[j] >= d[j]):
                    pass
                else:
                    flag = False
                    break
            if flag:
                ans.append(i)
        return ans

