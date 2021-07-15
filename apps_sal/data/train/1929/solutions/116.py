class TrieNode:
    def __init__(self, c):
        self.c = c
        self.children = {}
        self.is_word = False

class StreamChecker:

    def __init__(self, words: List[str]):
        self.char_list = []
        self.trie = TrieNode('')
        for word in words:
            node = self.trie
            for c in word[::-1]:
                if c not in node.children:
                    node.children[c] = TrieNode(c)
                node = node.children[c]
            node.is_word = True

    def query(self, letter: str) -> bool:
        self.char_list.append(letter)
        i = len(self.char_list) - 1
        node = self.trie
        while i >= 0:
            if self.char_list[i] not in node.children:
                break
            node = node.children[self.char_list[i]]
            if node.is_word:
                return True
            i -= 1
        return node.is_word


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

