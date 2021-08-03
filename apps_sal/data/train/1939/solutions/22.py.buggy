class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        wd_raw = set(wordlist)
        wd_low = {}
        wd_vow = {}
        
        for w in wordlist:
            wdLo = w.lower()
            wd_low.setdefault(wdLo, w)
            wd_vow.setdefault(self.devowel(wdLo), w)

        res = []
        
        
        for i,wd in enumerate(queries):
            qLow = wd.lower()
            qVow = self.devowel(qLow)
            
            if wd in wd_raw:
                res.append(wd)
            
            elif qLow in wd_low:
                res.append(wd_low[qLow])
                
            elif qVow in wd_vow:
                res.append(wd_vow[qVow])
                
            else:
                res.append(\"\")
                
        return res
    
    def devowel(self, wd):
        res = []
        for ch in wd:
            if ch in \"aeiou\":
                res.append(\"#\")
            else:
                res.append(ch)
                
        return \"\".join(res)
        
        
