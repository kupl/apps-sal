class TrieNode:
    def __init__(self):
        self.endOfWord=False
        self.children={}
class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie=TrieNode()
        self.stream=collections.deque()
        for word in words:
            node=self.trie
            for c in word[::-1]:
                if not c in node.children:
                    childNode=TrieNode()
                    node.children[c]=childNode
                node=node.children[c]
            node.endOfWord=True
       
    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        node=self.trie
        for c in self.stream:
            if not c in node.children:
                return False
            node=node.children[c]
            if node.endOfWord:
                return True
        return node.endOfWord

'''
class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie={}
        self.stream=collections.deque()
        for word in words:
            node=self.trie
            for ch in word[::-1]:
                if not ch in node:
                    node[ch]={}
                node=node[ch]
            node['$']=word
        
    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        node=self.trie
        for c in self.stream:
            if '$' in node:
                return True
            if not c in  node:
                return False
            node=node[c]
        #print('$' in node)
        return '$' in node
'''

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)


