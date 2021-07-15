class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        char_map = {char: i for i, char in enumerate(order)}
        for j in range(1, len(words)):
            prev, curr = words[j - 1], words[j]

            k = 0
            while k < min(len(prev), len(curr)):
                if prev[k] == curr[k]:
                    k += 1
                elif char_map[prev[k]] > char_map[curr[k]]:
                    return False
                else:
                    break
            if k >= len(curr):
                return False
        return True
