"""
from collections import defaultdict, deque
class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        if not wordlist or not queries:
            return []
        
        hm = defaultdict(list)
        for i, word in enumerate(wordlist):
            hm[word].append(i)
          
        ans = []
        for query in queries:
            if query in hm:
                ans.append(query)
            else:
                idx = self.capitalization(query, hm)
                if idx != float('inf'):
                    ans.append(wordlist[idx])
                else:
                    candidates = self.vowel_replace(query)
                    j = 0
                    min_idx = float('inf')
                    while j < len(candidates):
                        idx = self.capitalization(candidates[j], hm)
                        min_idx = min(min_idx, idx)
                        j += 1
                    if min_idx != float('inf'):
                        ans.append(wordlist[min_idx])
                    else:
                        ans.append('')
        return ans
                    
                        
    def capitalization(self, query, hm):
        idx = float('inf')
        for key in hm:
            if query.lower() == key.lower():
                idx = min(idx, hm[key][0])
        return idx
    
    from collections import deque
    def vowel_replace(self, query):
        candidates = []
        dq = deque([query.lower()])
        visited = set([query])
        while dq:
            curr = dq.popleft()
            candidates.append(curr)
            for i, c in enumerate(curr):        #curr, not query
                if c in 'aeiouAEIOU':       #c may be lower or upper
                    for x in 'aeiou':
                        if abs(ord(c) - ord(x)) != 32:  #c != x:
                            candidate = curr[:i] + x + curr[i + 1:]
                            if candidate.lower() not in visited:
                                dq.append(candidate)
                                visited.add(candidate.lower())
        return candidates[1:]
"""
"\nfrom collections import defaultdict\nclass Solution:\n    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:\n        if not wordlist or not queries:\n            return []\n        \n        hm = defaultdict(list)\n        for i, word in enumerate(wordlist):\n            hm[word].append(i)\n          \n        ans = []\n        for query in queries:\n            if query in hm:\n                ans.append(query)\n            else:\n                idx = self.capitalization(query, hm)\n                if idx != float('inf'):\n                    ans.append(wordlist[idx])\n                else:\n                    idx = self.vowel_replace(query, hm)\n                    if idx != float('inf'):\n                        ans.append(wordlist[idx])\n                    else:\n                        ans.append('')\n        return ans\n                    \n                        \n    def capitalization(self, query, hm):\n        idx = float('inf')\n        for key in hm:\n            if query.lower() == key.lower():\n                idx = min(idx, hm[key][0])\n        return idx\n    \n    def vowel_replace(self, query, hm):\n        idx = float('inf')\n        for key in hm:\n            if self.is_matched(query, key):     #key, not query\n                idx = min(idx, hm[key][0])\n        return idx\n    \n    def is_matched(self, str1, str2):\n        if len(str1) != len(str2):\n            return False\n        i, j = 0, 0\n        while i < len(str1) and j < len(str2):\n            if str1[i] not in 'aeiouAEIOU' and abs(ord(str1[i]) - ord(str2[j])) not in [0, 32]:     #辅音字母也可以有大小写\n                return False\n            if str1[i] in 'aeiouAEIOU' and str2[j] not in 'aeiouAEIOU':\n                return False\n            i += 1\n            j += 1\n        return True\n"


class Solution:

    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        if not wordlist or not queries:
            return []
        word_exact = set(wordlist)
        word_capital = defaultdict(list)
        word_vowel = defaultdict(list)
        for word in wordlist:
            word_lower = word.lower()
            word_capital[word_lower].append(word)
            word_vowel[self.devowel(word_lower)].append(word)
        ans = []
        for query in queries:
            if query in word_exact:
                ans.append(query)
            else:
                query_lower = query.lower()
                if query_lower in word_capital:
                    ans.append(word_capital[query_lower][0])
                elif self.devowel(query_lower) in word_vowel:
                    ans.append(word_vowel[self.devowel(query_lower)][0])
                else:
                    ans.append('')
        return ans

    def devowel(self, word):
        ans = ''
        for (i, c) in enumerate(word):
            if c in 'aeiou':
                ans += '*'
            else:
                ans += c
        return ans
