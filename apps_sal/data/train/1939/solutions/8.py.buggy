class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        if len(queries) == 0:
            return []
        Perfect = set(wordlist)
        Upper = {}
        Vowel = {}
        for word in wordlist:
            l = word.lower()
            if l not in Upper:
                Upper[l] = word
            temp = self.help(l)
            if temp not in Vowel:
                Vowel[temp] = word
    
        
        ans = []
        for word in queries:
            t = word.lower()
            temp = self.help(t)
            if word in Perfect:
                ans.append(word)
            elif t in Upper:
                ans.append(Upper[t])
            elif temp in Vowel:
                ans.append(Vowel[temp])
            else:
                ans.append(\"\")
        
        return ans
        
    def help(self, word):
        return \"\".join('*' if c in 'aeiou' else c
                           for c in word)
        
