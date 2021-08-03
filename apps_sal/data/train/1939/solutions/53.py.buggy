class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        capital = defaultdict(list)
        for word in wordlist:
            capital[word.lower()].append(word)
            
        vowels = defaultdict(list)
        for word in wordlist:
            newword = word
            for ch in \"aeiouAEIOU\":
                newword = newword.replace(ch, \"$\")
            vowels[newword.lower()].append(word)
        ans = []        
        for q in queries:
            if q in wordlist:
                ans.append(q)
            elif q.lower() in capital:
                ans.append(capital[q.lower()][0])
            else:
                newq = q
                for ch in \"aeiouAEIOU\":
                    newq = newq.replace(ch, \"$\")
                if newq.lower() in vowels:
                    ans.append(vowels[newq.lower()][0])
                else:
                    ans.append(\"\")
            
        return ans
