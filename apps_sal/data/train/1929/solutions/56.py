class Node:
    def __init__(self):
        self.c = collections.defaultdict(Node)
        self.e = 0
    
class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = Node()
        for w in words:
            temp = self.root
            for i in w:
                temp = temp.c[i]
            temp.e = 1
        self.w = []

    def query(self, letter: str) -> bool:
        # isIn = 0
        # temp = []
        self.w = [i.c[letter] for i in self.w+[self.root] if letter in i.c]
        return any(i.e for i in self.w)
#                     if letter in i.c:
#                         temp.append(i.c[letter])
#                         if not isIn:
#                             isIn = temp[-1].e
                
#         if letter in self.root.c:
#             temp.append(self.root.c[letter])
#             if not isIn:
#                 isIn = temp[-1].e
                
        # self.w = temp.copy()
        # print(i.c. for i in self.w)
        # return isIn
                
            


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)

