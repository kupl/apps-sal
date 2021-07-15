#replacing the vowels ('a', 'e', 'i', 'o', 'u') of the query word with any vowel individually
#return the first such match in the wordlist.
#important! Capitalization has a higher priority than Vowel Errors

#backtrack + deque, O(n*4^l), O(4^l), TLE
#notice that in all candidates, return the matched one with minimum index
'''
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
'''     

#check Consonants, O(n^2 * l), O(n), TLE
'''
from collections import defaultdict
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
                    idx = self.vowel_replace(query, hm)
                    if idx != float('inf'):
                        ans.append(wordlist[idx])
                    else:
                        ans.append('')
        return ans
                    
                        
    def capitalization(self, query, hm):
        idx = float('inf')
        for key in hm:
            if query.lower() == key.lower():
                idx = min(idx, hm[key][0])
        return idx
    
    def vowel_replace(self, query, hm):
        idx = float('inf')
        for key in hm:
            if self.is_matched(query, key):     #key, not query
                idx = min(idx, hm[key][0])
        return idx
    
    def is_matched(self, str1, str2):
        if len(str1) != len(str2):
            return False
        i, j = 0, 0
        while i < len(str1) and j < len(str2):
            if str1[i] not in 'aeiouAEIOU' and abs(ord(str1[i]) - ord(str2[j])) not in [0, 32]:     #辅音字母也可以有大小写
                return False
            if str1[i] in 'aeiouAEIOU' and str2[j] not in 'aeiouAEIOU':
                return False
            i += 1
            j += 1
        return True
'''

#3 hashmap/hashset
from collections import defaultdict
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
            word_vowel[self.devowel(word_lower)].append(word)   #key is word_lower
          
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
        for i, c in enumerate(word):
            if c in 'aeiou':
                ans += '*'
            else:
                ans += c
        return ans
                    
                        

                
        
        
            
        
                

