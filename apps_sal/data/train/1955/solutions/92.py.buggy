class union:
    def __init__(self):
        self.par = None
        self.rank = 0
    @staticmethod
    def parent(A):
        temp = A
        while A.par:
            A = A.par
        if temp != A:
            temp.par = A
        return A
    @staticmethod
    def fun(A,B):
        pA = union.parent(A)
        pB = union.parent(B)
        if pA != pB:
            if pA.rank > pB.rank:
                pB.par = pA
                pA.rank+=1
                return pB
            pA.par = pB
            pB.rank+=1
            return pA
        return None
            
class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        s = list(s)
        dic = {}
        par = set()
        for i in range(len(s)):
            temp =  union()
            dic[i] = temp
            par.add(temp)
        for i in pairs:
            temp = union.fun(dic[i[0]],dic[i[1]])
            if temp in par:
                par.remove(temp)
        
        if len(par) == 1:
            s.sort()
            return \"\".join(s)
        new = {}
        for i in par:
            new[i] = [[],0]
        for i in range(len(s)):
            par = union.parent(dic[i])
            new[par][0].append(s[i])
        for i in new.values():
            i[0].sort()
        ans =[]
        for i in range(len(s)):
            par = union.parent(dic[i])
            ind = new[par][1]
            new[par][1]+=1
            ans.append(new[par][0][ind])
        return \"\".join(ans)
        
        
