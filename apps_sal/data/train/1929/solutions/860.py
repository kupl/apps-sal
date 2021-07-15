class TrieNode:
    def __init__(self, char, isTerminal):
        self.char = char
        self.isTerminal = isTerminal
        self.nei = {}


class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = TrieNode(\"\", False)
        list(map(lambda x : self.insert(x[::-1], self.root),words ))
        self.q = \"\"
    def insert(self, word, root):
        if len(word) == 0:
            self.root.Isterminal = True
            return
        isTerminal = len(word)==1
        if word[0] in root.nei:
            root.nei[word[0]].isTerminal |= isTerminal
        else:
            child = TrieNode(word[0], isTerminal)
            root.nei[word[0]] = child
            
        if not isTerminal:
            self.insert(word[1:], root.nei[word[0]])

    def prinT(self, root, path):
        if root.isTerminal:
            print(path)
        for nei in root.nei:
            self.prinT( root.nei[nei], path[:] + root.nei[nei].char)
            
    def search(self, root, word):
        if not word:
            return root.isTerminal
        if root.isTerminal:
            return True
        
        if word[0] in root.nei:
            return self.search(root.nei[word[0]], word[1:])
        else:
            return False
        
    def query(self, letter: str) -> bool:
        self.q += letter
 
        
        if self.search(self.root, self.q[::-1]):
            return True
            
        return False
                
        # q = self.q
        # while q:
        #     print(q)
        #     if self.search(self.root, q):
        #         break
        #     q = q[1:]
        # self.q = q
        return len(self.q) >= 1 


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
