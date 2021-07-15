class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans=0
        from collections import Counter
        cd =Counter(chars)
        for w in words:
            wd=Counter(w)
            # print(wd & cd)
            if len(wd & cd) and len(list((wd & cd).elements())) == len(w):
                # print(list((wd & cd).elements())) 
                # print(w)
                ans+=len(w)
                
        return ans
            

