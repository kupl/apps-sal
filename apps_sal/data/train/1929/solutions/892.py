TERM_CHAR = '\\0'


def build_trie(words):
    trie = {}

    for word in words:
        current = trie
        for c in word:
            if c not in current:
                current[c] = {}
            current = current[c]

        current[TERM_CHAR] = True

    return trie


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = build_trie(words)

        self.trie_currents = []

    def query(self, letter: str) -> bool:
        found = False
        next_tries = []
        for current in self.trie_currents + [self.trie]:
            if letter in current:
                next_tries.append(current[letter])
                if current[letter].get(TERM_CHAR):
                    found = True

        self.trie_currents = next_tries

        return found
