class Node(object):
    def __init__(self):
        self.child = defaultdict(lambda: Node())
        self.leaf = False
    def add(self, word):
        #print(\"add word\", word)
        if len(word) == 0:
            self.leaf = True
        else:
            self.child[word[0]].add(word[1:])
    def query(self, word):
        #print(\"quering word\", word)
        if len(word) == 0:
            return self.leaf
        elif self.leaf:
            return True
        elif word[0] not in self.child:
            return False
        else:
            #print(\"word\",word)
            #print(word[0]) 
            #print(word[1:])
            return self.child[word[0]].query(word[1:])
            
class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = Node()
        self.queue = \"\"
        self.cur = None
        for w in words:
            self.root.add(list(reversed(w)))

    def query(self, letter: str) -> bool:
        self.queue = letter + self.queue
        

        return self.root.query(self.queue)











# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
