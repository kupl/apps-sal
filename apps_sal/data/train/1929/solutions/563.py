class StreamChecker:
    
    # I just used a trie, and inserted into it the reversals of the words. So by looking up something in the trie, I can tell if those letters are at the end of a word in the trie. But the leetcode results tell me my result is not that efficient, so I should check the Discuss tab to see better results. Maybe I am wasting time first doing the \"startsWith\" lookup, and if that is successful, having to begin again with the \"search\" lookup. There should be a way to have a startswith method that also tells you if it is or is not a word.
    # Following up on above comment, the code below corrects that \"problem\", but it still runs in the bottom 20% of python submissions. So I should read the Discuss tab!

    def __init__(self, words: List[str]):
        
        class Trie:
    
            class TreeNode:
        
                def __init__(self):
                    self.children = [None] * 26
                    self.isEndOfWord = False
    
            def __init__(self):
                \"\"\"
                Initialize your data structure here.
                \"\"\"
                self.root = self.TreeNode()
        

            def insert(self, word: str) -> None:
                \"\"\"
                Inserts a word into the trie.
                \"\"\"
                node = self.root
                for i in range(len(word)):
                    letter = word[i]
                    index = ord(letter) - ord('a')
                    if node.children[index] == None:
                        node.children[index] = self.TreeNode() 
                    if i == len(word) - 1:
                        node.children[index].isEndOfWord = True
                    node = node.children[index]
                
        
            def search(self, word: str) -> bool:
                \"\"\"
                Returns if the word is in the trie.
                \"\"\"
                node = self.root
                for i in range(len(word)):
                    letter = word[i]
                    index = ord(letter) - ord('a')
                    if node.children[index] == None:
                        return
                    else:
                        if i == len(word) - 1:
                            return node.children[index].isEndOfWord
                        node = node.children[index]
        

            def startsWith(self, prefix: str) -> bool:
                \"\"\"
                Returns if there is any word in the trie that starts with the given prefix.
                \"\"\"
                node = self.root
                for i in range(len(prefix)):
                    letter = prefix[i]
                    index = ord(letter) - ord('a')
                    if node.children[index] == None:
                        # return False
                        return (False, False)
                    else:
                        if i == len(prefix) - 1:
                            #return True
                            if node.children[index].isEndOfWord:
                                return (True, True)
                            else:
                                return (True, False)
                        node = node.children[index]
        
        self.trie = Trie()
        for word in words:
            rev = word[::-1]
            self.trie.insert(rev)
        self.letters = []

    def query(self, letter: str) -> bool:
        self.letters.append(letter)
        i = len(self.letters) -1
        res = \"\"
        while i >= 0:
            res += self.letters[i]
            starts, isWord = self.trie.startsWith(res)
            if not starts:
                return False
            if isWord:
                return True
            #if not self.trie.startsWith(res):
            #    return False
            #else:
            #    if self.trie.search(res):
            #        return True
            i -= 1


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
