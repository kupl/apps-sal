class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = {}
        for word in words:
            node = self.root
            for c in word:
                node = node.setdefault(c, {})
            node['is_end'] = True
        self.running = []

    def query(self, letter: str) -> bool:
        survived = []
        found = False

        if letter in self.root:
            self.running.append(self.root)

        for node in self.running:
            if letter in node:
                survived.append(node[letter])
                found = found or 'is_end' in survived[-1]

        self.running = survived
        return found
