class Node:
    def __init__(self, val=None, is_end=False):
        self.child = dict()
        self.val = val
        self.is_end = is_end


class StreamChecker:

    def __init__(self, words: List[str]):
        self.root = Node()
        for w in words:
            tmp = self.root
            for l in w[::-1]:
                if l not in tmp.child:
                    tmp.child[l] = Node(val=l)
                tmp = tmp.child[l]
            tmp.is_end = True
        self.q = []

    def query(self, letter: str) -> bool:
        if len(self.q) >= 2000:
            self.q.pop(0)
        self.q.append(letter)
        tmp = self.root
        for i in self.q[::-1]:
            if i not in tmp.child:
                return False
            tmp = tmp.child[i]
            if tmp.is_end:
                return True
        return tmp.is_end


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
