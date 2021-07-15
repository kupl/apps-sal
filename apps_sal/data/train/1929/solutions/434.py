class Node:
    def __init__(self):
        self.children = [None]*26
        self.isWord = False
    def calculateIndex(self,char):
        return ord(char)-ord('a')

class Trie:
    def __init__(self):
        self.root = Node()
    def addWordInReverse(self,word):
        wordLength = len(word)
        currentNode = self.root
        for i in range(wordLength-1,-1,-1):
            currentChar = word[i]
            currentIndex = currentNode.calculateIndex(currentChar)
            if(currentNode.children[currentIndex] == None):
                currentNode.children[currentIndex] = Node()
            currentNode = currentNode.children[currentIndex]
        currentNode.isWord = True;
class StreamChecker:

    def __init__(self, words: List[str]):
        self.stream = []
        self.reverseTrie = Trie()##no new keyword before object instantiation
        for word in words:
            self.reverseTrie.addWordInReverse(word)

    def query(self, letter: str) -> bool:
        self.stream.append(letter)
        streamLength = len(self.stream)
        currentNode = self.reverseTrie.root
        for i in range(streamLength-1,-1,-1):
            currentChar = self.stream[i]
            currentIndex = currentNode.calculateIndex(currentChar)
            if(currentNode.children[currentIndex] != None):
                currentNode = currentNode.children[currentIndex]
                if(currentNode.isWord):
                    return True
            else:
                return False
        return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

