class StreamChecker:

    def __init__(self, words: List[str]):
        self.curQuery = ''
        self.Trie = Trie()
        for word in words:
            newWord = word[::-1]
            self.Trie.insert(newWord)

    def query(self, letter: str) -> bool:
        self.curQuery = letter + self.curQuery
        curNode = self.Trie.root
        i = 0
        while curNode and i<len(self.curQuery):
            
            curLetter = self.curQuery[i]
            ind = ord(curLetter) - ord('a')
            curNode = curNode.children[ind]
            if not curNode:
                return False
            if curNode.isWord:
                return True
            
            i += 1
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

class Trie:
    def __init__(self):
        self.root = Node()
    def insert(self, word):
        curNode = self.root
        for i in range(len(word)):
            ind = ord(word[i])-ord('a')
            if curNode.children[ind]:
                curNode = curNode.children[ind]
            else:
                curNode.children[ind] = Node()
                curNode = curNode.children[ind]
        curNode.isWord = True
        return
                
        
class Node:
    def __init__(self):
        self.children = [None] * 26
        self.isWord = False
