class Node:
    def __init__(self, x):
        self.val=x
        self.next={}
        self.word=False
class Trie:
    def __init__(self):
        self.root=Node(None)
    
    def add(self, word):
        root=self.root
        for w in word:
            if w not in root.__next__:
                node=Node(w)
                root.next[w]=node
            root=root.next[w]
        root.word=True
        
class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie=Trie()
        self.key={}
        self.pre=set([])
        for i in words:
            self.trie.add(i)

    def query(self, letter: str) -> bool:
        root=self.trie.root
        temp=set([])
        ans=False
        for i in self.pre:
            if letter in i.__next__:
                node=i.next[letter]
                if node.word:
                    ans=True
                temp.add(node)
        if letter in root.__next__:
            node=root.next[letter]
            temp.add(node)
            if node.word:
                ans=True
        self.pre=temp
        return ans

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

