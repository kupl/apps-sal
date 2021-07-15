class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        d=Counter(chars)
        ans=0
        for w in words:
            temp=d.copy()
            b=True
            for i in w:
                try:
                    if temp[i]!=0:
                        temp[i]-=1
                    else:
                        b=False
                        break
                    
                except:
                    b=False
                    break
            if b:
                ans+=len(w)
        return ans
