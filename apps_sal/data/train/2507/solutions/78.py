class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        
        char_count = collections.Counter(chars)
        total = 0
        for word in words:
            if not collections.Counter(word) - char_count:
                total += len(word)
                
        return total
