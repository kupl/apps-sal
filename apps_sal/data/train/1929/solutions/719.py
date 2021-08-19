class StreamChecker:

    def __init__(self, words: List[str]):
        head = {}
        for w in words:
            current = head
            for c in w:
                if c not in current:
                    current[c] = {}
                current = current[c]
            current['X'] = None
        self.head = head
        self.current = [head]

    def query(self, letter: str) -> bool:
        new_current = [self.head]
        for e in self.current:
            if letter in e:
                new_current.append(e[letter])
        self.current = new_current
        for e in new_current:
            if 'X' in e:
                return True
        return False
