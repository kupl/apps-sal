class TrieNode:
    def __init__(self):
        self.neighbor = {}
        self.isend = False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie_root = TrieNode()
        self.letters = []
        self.max_len = max(list(map(len, words)))

        for word in words:
            curr = self.trie_root
            for c in word[::-1]:
                if c not in curr.neighbor:
                    curr.neighbor[c] = TrieNode()
                curr = curr.neighbor[c]
            curr.isend = True

    def query(self, letter: str) -> bool:
        self.letters.append(letter)
        self.letters = self.letters[max(0, len(self.letters) - self.max_len):]

        curr = self.trie_root
        for l in self.letters[::-1]:
            if l in curr.neighbor:
                curr = curr.neighbor[l]
                if curr.isend:
                    return True
            else:
                return False
        return False
