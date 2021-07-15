class Node:
    
    def __init__(self):
        self.children = {}
        self.isEnd = False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Node()
        for w in words:
            if(len(w) > 0):
                self.insert(w[::-1])
        self.queryStack = []
    
    def insert(self, word):
        root = self.trie
        self.insertWord(root, word, 0)
        
    
    def insertWord(self, curNode, word, index):
        if(index >= len(word)):
            curNode.isEnd = True
        else:
            curChar = word[index]
            if(curChar not in curNode.children):
                newNode = Node()
                curNode.children[curChar] = newNode
            self.insertWord(curNode.children[curChar], word, index+1)
    
    def findIfPresent(self, curNode, index):
        if(curNode.isEnd):
            return True
        if(index < 0):
            return False
        if(self.queryStack[index] not in curNode.children):
            return False
        return self.findIfPresent(curNode.children[self.queryStack[index]], index-1)
    
    def query(self, letter: str) -> bool:
        self.queryStack.append(letter)
        root = self.trie
        return self.findIfPresent(root, len(self.queryStack)-1)
        
        
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

