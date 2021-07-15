from collections import deque

class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.eow = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        
    def charToIndex(self, _char):
        return ord(_char) - ord('a')
    
    def insert(self, word):
        node = self.root
        l = len(word)
        for i in range(l):
            idx = self.charToIndex(word[i])
            if node.children[idx] == None:
                node.children[idx] = TrieNode()
            node = node.children[idx]
        node.eow = True
        
    def search(self, word):
        node = self.root
        l = len(word)
        for i in range(l):
            idx = self.charToIndex(word[i])
            if node.children[idx] != None:
                node = node.children[idx]
            else:
                return False
            if node.eow:
                return True
        return node!=None and node.eow


class StreamChecker:
    def __init__(self, words: List[str]):
        self.words = words
        self.trie = Trie()
        for word in self.words:
            # print(word[::-1])
            self.trie.insert(word[::-1])

        self.longest = len(max(words, key=len))
        self.data = deque([], maxlen=self.longest)
        

    def query(self, letter: str) -> bool:
        if self.data.count == self.longest:
                popped = self.data.pop()
        self.data.appendleft(letter)
        # print(\"\".join(self.data))
        if self.trie != None and self.trie.root.children[ord(letter)-ord('a')] != None:
            return self.trie.search(\"\".join(self.data))
        else:
            return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
