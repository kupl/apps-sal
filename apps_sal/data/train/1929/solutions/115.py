class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = dict()
        self.input = ''

        for word in words:
            ptr = self.trie
            for w in word[::-1]:
                if w not in list(ptr.keys()):
                    ptr[w] = dict()
                ptr = ptr[w]
            ptr['$'] = word

    def query(self, letter: str) -> bool:
        self.input += letter
        node = self.trie
        for index in range(len(self.input)):
            ch = self.input[-(index + 1)]
            if '$' in list(node.keys()):
                return True
            elif ch not in list(node.keys()):
                return False
            node = node[ch]
        return '$' in list(node.keys())
