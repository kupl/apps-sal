from collections import Counter


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        return bruteforce_with_counter(words, chars)


def bruteforce_with_counter(words, chars):
    counter = Counter(chars)
    return sum(len(w) for w in words if not (Counter(w) - counter))
