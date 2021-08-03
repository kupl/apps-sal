from collections import defaultdict
class Node:
    def __init__(self):
        self._childrn = defaultdict()
        self.wef = 0

class StreamChecker(Node):
    def __init__(self, words: List[str]):
        self.root = Node()
        self.wordh = \"\"
        
        for i in words:
            self.storeW(i)
            
    def _ind(self,ch):
        return(ord(ch) - ord('a'))

    def storeW(self,word):
        cur = self.root
        for i in word[::-1]:
            ind = self._ind(i)
            if ind not in cur._childrn:
                cur._childrn[ind] = Node()
            cur = cur._childrn[ind]
            
        cur.wef = True

    def query(self, letter: str) -> bool:
        cur = self.root
        self.wordh = letter + self.wordh
        for i in self.wordh:
            ind = self._ind(i)
            if not cur._childrn.get(ind):
                return(False)
            else:
                cur = cur._childrn.get(ind)
                if cur.wef:
                    return(True)
            
        
        return(False)
        



# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
