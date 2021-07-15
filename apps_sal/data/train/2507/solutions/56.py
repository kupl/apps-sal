class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d={}
        c=0
        for i in chars:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in words:
            dd={}
            for j in i:
                if j in dd:
                    dd[j]+=1
                else:
                    dd[j]=1
            c1=0
            for x in dd.keys():
                if x in d:
                    if d[x]>=dd[x]:
                        c1+=dd[x]
                    else:
                        c1=0
                        break
                else:
                    c1=0
                    break
            c+=c1
        return c
