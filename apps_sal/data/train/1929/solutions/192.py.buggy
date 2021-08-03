from collections import deque

class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.nextFail = None
        self.suffixMatches = []

    def add(self, word, index=0):
        #print(word)
        if len(word) == index:
            self.boundary = True
            self.suffixMatches = [word]
            return
        c = word[index]
        if self.children.get(c, None) is None:
            self.children[c] = TrieNode()
        self.children[c].add(word, index + 1)
    def __str__(self):
        return self.__str2()

    def __str2(self, indent=0):
        space = \"  \"*indent
        return \"{}TrieNode(h={}, B={}, nf={},\
{}\".format(
            space,
            hash(self), self.suffixMatches, hash(self.nextFail) if self.nextFail else \"None\", \"\".join(space + k + \": \" + v.__str2(indent+1) + \"\
\" for k, v in self.children.items()),
            space
        ) + space + \")\"


class AhoTrie(object):
    def __init__(self, words):
        self.root = TrieNode()
        for word in words:
            self.root.add(word)
        self.__oho()

    def __oho(self):
        q = deque()
        for c, node in self.root.children.items():
            node.nextFail = self.root
            q.append(node)
        while len(q) > 0:
            node = q.popleft()
            
            for c, child in node.children.items():
                nextFail = node.nextFail
                while not nextFail.children.get(c) and nextFail is not self.root:
                    nextFail = nextFail.nextFail
                if not nextFail.children.get(c):
                    child.nextFail = nextFail
                else:
                    child.nextFail = nextFail.children.get(c)

                q.append(child)
                #child.nextFail = node.nextFail.children.get(c, node.nextFail)
                if  True: #child.suffixMatches:
                    nextFail = child.nextFail
                    while nextFail is not self.root and not nextFail.suffixMatches:
                        nextFail = nextFail.nextFail
                    if nextFail is not self.root:
                        child.suffixMatches.extend(nextFail.suffixMatches)





class StreamChecker:

    def __init__(self, words: List[str]):
        print(words)
        self.trie = AhoTrie(words) 
        self.root = self.trie.root
        self.cur = self.root
        #print(self.root)
        

    def query(self, letter: str) -> bool:
        
        
        while not self.cur.children.get(letter) and self.cur is not self.root:
            self.cur = self.cur.nextFail
        #print(hash(self.cur))
        if self.cur.children.get(letter):
            self.cur = self.cur.children[letter]
            temp = self.cur
            #while temp is not self.root:
            if temp.suffixMatches:
                return True
             #  temp = temp.nextFail
        return False
            
        
        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
