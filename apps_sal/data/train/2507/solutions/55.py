class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans=0
        for w in words:
            tc=chars
            flag=True
            for l in w:
                if l in tc:
                    tc = tc.replace(l,'',1)
                else:
                    flag=False
            if flag:
                ans+=len(w)
        return ans
