class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        words = sentence.split(' ')
        match = [i for i,w in enumerate(words) if w.startswith(searchWord)]
        if not match:
            return -1
        return match[0]+1
