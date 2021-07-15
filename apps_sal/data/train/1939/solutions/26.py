class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        set_case_sensitive = set()
        dict_case_insensitive = {}
        dict_case_vowel_insensitive = {}
                
        def replace_all(text):
            for c in \"aeiou\":
                text = text.replace(c, '*')
            return text
        
        for w in wordlist:
            set_case_sensitive.add(w)
            lw = w.lower()
            if lw not in dict_case_insensitive:
                dict_case_insensitive[lw] = w
            lwv = replace_all(lw)
            if lwv not in dict_case_vowel_insensitive:
                dict_case_vowel_insensitive[lwv] = w 
            
        res = []
        for q in queries:
            lq = q.lower()
            if q in set_case_sensitive:
                res.append(q)
            elif lq in dict_case_insensitive:
                res.append(dict_case_insensitive[lq])
            else:
                without_v = replace_all(lq)
                if without_v in dict_case_vowel_insensitive:
                    res.append(dict_case_vowel_insensitive[without_v])
                else:
                    res.append(\"\")
                    
        return res
                
        
                
