class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        cur = self.root
        for c in word:
            if cur.children[ord(c) - ord('a')] == None:
                cur.children[ord(c) - ord('a')] = TrieNode()
            cur = cur.children[ord(c) - ord('a')]
        cur.isWord = True

    def search(self, word):

        # return self.root.children[ord(word[0]) - ord('a')]

        return self.__searchHelper(self.root, word, 0)

    def __searchHelper(self, cur, word, word_index):
        if len(word) == word_index:
            return cur.isWord
        if cur.isWord:
            return True

        char = word[word_index]
        temp = cur.children[ord(char) - ord('a')]

        return temp != None and self.__searchHelper(temp, word, word_index + 1)


class StreamChecker:

    def __init__(self, words: List[str]):
        self.storage = Trie()
        self.prefix = ''

        for word in words:
            self.storage.add(word[::-1])

    def query(self, letter: str) -> bool:
        self.prefix += letter
        return self.storage.search(self.prefix[::-1])


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
