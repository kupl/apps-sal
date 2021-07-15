class Solution:
    def spellchecker(self, words, queries):
        def vowels(s):
            return ''.join('*' if c in 'AEIOU' else c for c in s)
        wordset=set(words)
        cap={w.upper():w for w in reversed(words)}
        vow={vowels(w.upper()):w for w in reversed(words)}
        
        ans=[]
        for q in queries:
            if q in wordset:
                ans.append(q)
                continue
            q=q.upper()
            if q in cap:
                ans.append(cap[q])
                continue
            q=vowels(q)
            if q in vow:
                ans.append(vow[q])
                continue
            ans.append('')
        
        return ans
