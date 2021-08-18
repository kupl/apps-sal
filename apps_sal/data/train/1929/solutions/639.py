class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = {}
        self.memo = ''

        for w in words:
            ptr = self.root
            for c in w[::-1]:
                if c not in ptr:
                    ptr[c] = {}
                ptr = ptr[c]
            ptr['

    def query(self, letter: str) -> bool:
        self.memo += letter
        ptr = self.root
        for c in self.memo[::-1]:
            if c not in ptr:
                return False
            ptr = ptr[c]
            if '
                return True

        return False
