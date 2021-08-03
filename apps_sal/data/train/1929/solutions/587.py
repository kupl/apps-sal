class TrieNode:
    def __init__(self, parent):
        self.parent = parent
        self.children = collections.defaultdict(lambda: TrieNode(self))
        self.c = None


class Trie:

    def __init__(self):
        self.root = TrieNode(None)
        self.ends = collections.defaultdict(list)

    def add(self, word):
        curr = self.root
        for c in word:
            curr = curr.children[c]
            curr.c = c
        if len(word) > 0:
            self.ends[word[-1]].append(curr)

    def isMember(self, letters):
        if letters[-1] not in self.ends:
            return False
        poss = self.ends[letters[-1]]

        for p in poss:
            curr = p
            index = len(letters) - 2
            while curr and index >= 0:
                curr = curr.parent
                if curr == self.root:
                    return True
                if curr.c != letters[index]:
                    curr = None
                index -= 1
            if index == -1 and curr != None and curr.parent == self.root:
                return True
        return False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for w in words:
            self.trie.add(w)
        self.maxLen = max(list([len(x) for x in words]))
        self.queries = []

    def query(self, letter: str) -> bool:
        self.queries.append(letter)
        if len(self.queries) > self.maxLen:
            del self.queries[0]
        return self.trie.isMember(self.queries)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
