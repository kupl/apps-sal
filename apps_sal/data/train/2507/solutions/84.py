class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        char_map = {c: chars.count(c) for c in set(chars)}
        count = 0
        for w in words:
            good = True
            for c in w:
                if c not in char_map.keys() or w.count(c) > char_map[c]:
                    good = False
            if good:
                count += len(w)
        return count
