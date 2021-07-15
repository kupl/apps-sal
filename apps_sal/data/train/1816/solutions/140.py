class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        t=[int(s[:2])*60+int(s[3:]) for s in keyTime]
        l=sorted(zip(keyName,t)) 
        d=collections.defaultdict(list)
        for i,j in l: d[i]+=[j]
        return [s for s,l in list(d.items()) if any(j-i<=60 for i,j in zip(l[:-2],l[2:]))]       


