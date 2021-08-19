class StreamChecker:

    def __init__(self, words: List[str]):
        self.ord_a = ord('a')
        stop_ord = ord('z') - self.ord_a + 1
        self.trie = [None] * stop_ord
        self.trie.append(False)
        ord_l = 0
        for word in words:
            current = self.trie
            for l in reversed(word):
                ord_l = ord(l) - self.ord_a
                if current[ord_l] is None:
                    current[ord_l] = [None] * stop_ord
                    current[ord_l].append(False)
                current = current[ord_l]
            current[-1] = True
        self.stream = []

    def query(self, letter: str) -> bool:
        result = False
        ord_l = ord(letter) - self.ord_a
        self.stream.append(ord_l)
        current = self.trie
        for l in self.stream[::-1]:
            current = current[l]
            if current is None:
                return False
            elif current[-1]:
                return True
        return current[-1]
