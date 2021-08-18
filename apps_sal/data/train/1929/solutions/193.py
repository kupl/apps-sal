class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = {}
        for word in words:
            level = self.trie
            for char in reversed(word):
                if char not in level:
                    level.update({char: {}})
                level = level[char]
            level.update({'.': {}})

        self.stream = ''

    def query(self, letter: str) -> bool:
        self.stream += letter
        level = self.trie
        for char in reversed(self.stream):
            if '.' in level:
                return True
            if char not in level:
                return False
            level = level[char]
        if '.' in level:
            return True
        return False
