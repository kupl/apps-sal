
class Solution:
    from collections import defaultdict
    def getFolderNames(self, lis: List[str]) -> List[str]:
        s = set()
        ans=[]
        d=defaultdict(int)
        for i in lis:
            k=d[i]
            cur = i
            while cur in s:
                k+=1
                cur = '%s(%d)' % (i, k)
            d[i]=k
            s.add(cur)
            ans.append(cur)
        return ans
