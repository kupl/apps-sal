from collections import Counter
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        for i in range(len(words)):
            if Counter(words[i]) & Counter(chars) == Counter(words[i]):
                ans += len(words[i])
                
        return ans

