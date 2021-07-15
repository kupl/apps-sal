
#5:58
class TrieNode:
    def __init__(self):
        self.val = 0
        self.children = [None]*26
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word):
        curr = self.root
        for char in word:
            if curr.children[ord(char) - ord('a')] is None:
                curr.children[ord(char) - ord('a')] = TrieNode()
            curr = curr.children[ord(char) - ord('a')]
        curr.val = 1
        
    def searchWord(self, word):
        curr = self.root
        for char in word:
            if curr.children[ord(char) - ord('a')] is None:
                return False
            curr = curr.children[ord(char) - ord('a')]
            if curr.val == 1:
                return True
        return False
        

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        max_len = 0
        for word in words:
            max_len = max(max_len, len(word))
            self.trie.addWord(\"\".join([x for x in reversed(word)]))
        self.query_text = \"\"
        self.max_len = max_len

    def query(self, letter: str) -> bool:
        self.query_text += letter
        if len(self.query_text) >self.max_len:
            self.query_text = self.query_text[1:]
        reversed_query = \"\".join([x for x in reversed(self.query_text)])
        return self.trie.searchWord(reversed_query)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
