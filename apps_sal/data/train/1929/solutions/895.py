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
        #self.paths = []
        #self.start = 0
        self.stream = []

    def query(self, letter: str) -> bool:

        result = False
        # print()
        # print(\"letter: {0}\".format(letter))
        # print(self.paths)
        ord_l = ord(letter) - self.ord_a
        self.stream.append(ord_l)
        # while (self.start+1) < len(self.paths) and self.paths[self.start] is None:
        #    self.start+=1
        # for path in range(self.start,len(self.paths)):
        #    if not self.paths[path] is None:
        #        if not self.paths[path][ord_l] is None:
        #            self.paths[path] = self.paths[path][ord_l]
        #            result = result | self.paths[path][-1]
        #        else:
        #            self.paths[path] = None
        # if not self.trie[ord_l] is None:
        #    self.paths.append(self.trie[ord_l])
        #    result = self.trie[ord_l][-1] | result
        # print(self.paths)
        current = self.trie
        for l in self.stream[::-1]:
            current = current[l]
            if current is None:
                return False
            elif current[-1]:
                return True
        return current[-1]


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
