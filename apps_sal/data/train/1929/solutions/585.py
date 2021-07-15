class Trie:
    
    def __init__(self):
        self.dict = {}
        self.leaf = False
        
    def addWord(self,word):
        newTrie = Trie()
        if word[0] in self.dict:
            newTrie = self.dict[word[0]]
        else:
            self.dict[word[0]] = newTrie
        if len(word) == 1:
            newTrie.leaf = True
        else:
            newTrie.addWord(word[1:])
            
    
# class Node:
    
#     def __init__(self,val,left=None,right=None):
#         self.val = val
#         self.left = left; self.right = right
    
class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        self.queryStr = ''
        for word in words:
            self.trie.addWord(word[::-1])
        #print(self.trie)
        
    def query(self, letter: str) -> bool:
        self.queryStr += letter
        curTrie = self.trie
        #print(letter)
        for ch in self.queryStr[::-1]:
            #print('current ch : {}'.format(ch))
            if ch in curTrie.dict:
                curTrie = curTrie.dict[ch]
                if curTrie.leaf == True:
                    return True
                #print(curTrie.dict)
                #print(curTrie.leaf)
            else:
                #print('return false')
                return False


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

