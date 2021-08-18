def ctoi(c):
    return ord(c) - 97


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = [None] * 27
        for w in words:
            curr_trie = self.trie
            for c in w:
                c_idx = ctoi(c)
                if not curr_trie[c_idx]:
                    curr_trie[c_idx] = [None] * 27
                curr_trie = curr_trie[c_idx]
            curr_trie[-1] = True

        self.ptrs = []

    def query(self, letter: str) -> bool:
        found = False
        self.ptrs.append(self.trie)
        new_ptrs = []
        c_idx = ctoi(letter)

        for ptr in self.ptrs:
            if ptr[c_idx]:
                new_ptrs.append(ptr[c_idx])
                if ptr[c_idx][-1]:
                    found = True

        self.ptrs = new_ptrs

        return found
