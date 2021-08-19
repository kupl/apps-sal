class TrieNode:

    def __init__(self):
        self.endOfWord = False
        self.children = {}


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = TrieNode()
        self.stream = collections.deque()
        for word in words:
            node = self.trie
            for c in word[::-1]:
                if not c in node.children:
                    childNode = TrieNode()
                    node.children[c] = childNode
                node = node.children[c]
            node.endOfWord = True

    def query(self, letter: str) -> bool:
        self.stream.appendleft(letter)
        node = self.trie
        for c in self.stream:
            if not c in node.children:
                return False
            node = node.children[c]
            if node.endOfWord:
                return True
        return False


"\nclass StreamChecker:\n    def __init__(self, words: List[str]):\n        self.trie={}\n        self.stream=collections.deque()\n        for word in words:\n            node=self.trie\n            for ch in word[::-1]:\n                if not ch in node:\n                    node[ch]={}\n                node=node[ch]\n            node['$']=word\n        \n    def query(self, letter: str) -> bool:\n        self.stream.appendleft(letter)\n        node=self.trie\n        for c in self.stream:\n            if '$' in node:\n                return True\n            if not c in  node:\n                return False\n            node=node[c]\n        #print('$' in node)\n        return '$' in node\n"
