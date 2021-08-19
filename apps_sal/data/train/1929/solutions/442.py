class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            node = self.trie  # reset for each word
            for ch in reversed(word):
                node.setdefault(ch, {})
                node = node[ch]
            node['#'] = {}
        self.letters = []

    def query(self, letter: str) -> bool:
        self.letters.insert(0, letter)
        node = self.trie
        for ch in self.letters:
            if ch in node:
                node = node[ch]
                if '#' in node:  # found it, no need to go deeper
                    return True
            else:
                break  # use the last found node
        return False
