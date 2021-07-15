class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        b=collections.Counter(B[0])
        f=collections.defaultdict(int)
        for x in B:
            p=Counter(x)
            for k in list(p.keys()):
                if k in b:
                    b[k]=max(p[k],b[k])
                else:
                    b[k]=p[k]
        res=[]
        for word in A:
            word_counter=collections.Counter(word)
            add=True
            for i in b:
                if i not in word_counter or b[i]>word_counter[i]:
                    add=False
            if add:
                res.append(word)
        return res    
                    

