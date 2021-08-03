import collections


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        self.stream = collections.deque()
        self.prefixes = []
        for w in words:
            ptr = self.trie
            for c in w:
                if c not in ptr:
                    ptr[c] = {}
                ptr = ptr[c]
            ptr['#'] = w

    def _find_word(self, k: int) -> bool:
        ptr = self.trie
        for c in list(self.stream)[-k:]:
            if c not in ptr:
                return False
            ptr = ptr[c]
        return '#' in ptr

    def query(self, letter: str) -> bool:
        # print(letter)
        if letter in self.trie:
            self.prefixes.append(self.trie)
        valid_prefixes, found = [], False
        for i, ptr in enumerate(self.prefixes):
            # print(f'  {ptr}')
            if letter in ptr:
                ptr = ptr[letter]
                valid_prefixes.append(ptr)
                if '#' in ptr:
                    found = True
        self.prefixes = valid_prefixes
        return found


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
