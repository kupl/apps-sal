class Solution:
    def compare(self,d,d1):
        for i in d:
            if(i not in d1 or d[i]>d1[i]):
                return False
        return True
    
    def wordSubsets(self, a: List[str], b: List[str]) -> List[str]:
        bgroup = {}
        for i in b:
            d = {}
            for j in i:
                if j in d:
                    d[j]+=1
                else:
                    d[j] = 1
            for j in d:
                if j not in bgroup:
                    bgroup[j] = d[j]
                else:
                    bgroup[j] = max(bgroup[j],d[j])
        ans = []
        for i in a:
            d1 = {}
            for j in i:
                if j in d1:
                    d1[j]+=1
                else:
                    d1[j] = 1
            if(self.compare(bgroup,d1)):
                ans.append(i)
        return  ans
