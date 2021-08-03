class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = 0
        f = 1
        for s in words:
            f = 1
            for c in s:
                if s.count(c) > chars.count(c):
                    f = 0
            if f:
                print(s)
                count += len(s)
        return count
