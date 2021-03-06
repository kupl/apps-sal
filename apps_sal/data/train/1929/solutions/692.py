class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = {}
        for word in words:
            node = self.root
            for char in word:
                if char not in node:
                    node[char] = {}
                node = node[char]
            node['#'] = 1
        self.candidates = []

    def query(self, letter: str) -> bool:
        found = False
        new_candidates = []
        self.candidates.append(self.root)
        for node in self.candidates:
            if letter in node:
                node = node[letter]
                new_candidates.append(node)
                if '#' in node:
                    found = True
        self.candidates = new_candidates
        return found
