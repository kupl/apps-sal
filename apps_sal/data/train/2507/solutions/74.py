from collections import Counter


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        return bruteforce_with_counter(words, chars)

# words=[\"cat\", \"bat\", \"mat\", \"battle\"], chars=[\"catbtle\"]
# cat vs catbtle
# mat vs catbtle


def bruteforce_with_counter(words, chars):
    counter = Counter(chars)
    # BUG. SHIT.
    # return sum(len(w) for w in words if min((counter - Counter(w)).values()) >= 0)
    # return sum(len(w) for w in words if max((Counter(w)-counter).values()) <= 0)
    return sum(len(w) for w in words if not (Counter(w) - counter))
