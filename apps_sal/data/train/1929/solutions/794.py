\"\"\"
class Node:
    def __init__(self, c):
        self.char = c
        self.pointers = {}
        self.wordEnd = False

class Trie:
    def __init__(self):
        self.d = {}

    def insert(self, word: str) -> None:
        if not word:
            return
        
        if word[0] not in self.d:
            self.d[word[0]] = Node(word[0])
            
        if len(word) > 1:
            n = self.d[word[0]]
            
            for j, c in enumerate(word[1:]):
                if c in n.pointers:
                    n = n.pointers[c]
                else:
                    n_ = Node(c)
                    n.pointers[c] = n_
                    n = n_
                
                if j+1 == len(word)-1:
                    n.wordEnd = True
        else:
            self.d[word[0]].wordEnd = True

class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for w in words:
            self.trie.insert(w)
        
        self.curNode = None
        
        self.q = []
        

    def getNext(self, letter):        
        if not self.q:
            if letter in self.trie.d:
                self.q.append(self.trie.d[letter])
        else:
            q2 = []
            
            visited =  set()

            for node in self.q:
                for p in node.pointers:                    
                    newNode = node.pointers[p]
                    
                    if newNode in visited:
                        #print (\"duplicate\")
                        continue

                    if newNode.char == letter:
                        q2.append(newNode)
                        visited.add(newNode)
            
            for node in self.trie.d:
                for p in self.trie.d:                    
                    newNode = self.trie.d[p]
                    
                    if newNode in visited:
                        #print (\"duplicate\")
                        continue

                    if newNode.char == letter:
                        q2.append(newNode)
                        visited.add(newNode)

            self.q = q2
        
        
    def query(self, letter: str) -> bool:
        self.getNext(letter)
        return any([x.wordEnd for x in self.q])
\"\"\"

class StreamChecker(object):

    def __init__(self, words):
        T = lambda: collections.defaultdict(T)
        self.trie = T()
        for w in words: reduce(dict.__getitem__, w, self.trie)['#'] = True
        self.waiting = []

    def query(self, letter):
        self.waiting = [node[letter] for node in self.waiting + [self.trie] if letter in node]
        return any(\"#\" in node for node in self.waiting)


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

