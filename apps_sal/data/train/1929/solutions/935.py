import collections


class StreamChecker:

    def __init__(self, words: List[str]):

        self.Trie = {}

        for word in words:
            parent = self.Trie
            for char in word:
                parent = parent.setdefault(char, {})
            parent['$'] = None

        self.waitList = []

    def query(self, letter: str) -> bool:

        waitList = []

        if letter in self.Trie:
            waitList.append(self.Trie[letter])

        for currTrie in self.waitList:
            if letter in currTrie:
                waitList.append(currTrie[letter])

        self.waitList = waitList

        return any('$' in item for item in waitList)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
