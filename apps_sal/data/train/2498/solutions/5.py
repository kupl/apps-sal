class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        index_lookup = {char: i for i, char in enumerate(order)}
        for i in range(len(words) - 1):
            first, second = words[i:i + 2]
            for j in range(min(len(first), len(second))):
                if first[j] != second[j]:
                    if index_lookup[first[j]] > index_lookup[second[j]]:
                        return False
                    break
            else:
                if len(first) > len(second):
                    return False
        return True
