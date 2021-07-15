class StreamChecker:
    class Node:
        def __init__(self, isWord=False):
            self.children = [None]*26
            self.isWord = isWord
            
    import queue
    def __init__(self, words: List[str]):
        self.root = self.Node()
        self.N = 0 # maxWordLength
        for word in words:
            self.N = max(self.N, len(word))
            cursor = self.root
            for c in reversed(word):
                if next := cursor.children[ord(c)-97]:
                    cursor = next
                else:
                    newNode = self.Node()
                    cursor.children[ord(c)-97] = newNode
                    cursor = newNode
            cursor.isWord = True
        
        # self.queue = queue.Queue(maxsize=maxWordLen)
        self.buffer = [None]*self.N
        self.bIdx = self.N

    def query(self, letter: str) -> bool:
        # advance or terminate cursors
        self.bIdx = (self.bIdx - 1) % self.N
        self.buffer[self.bIdx] = letter
        
        cursor = self.root
        for i in range(self.bIdx, self.N):
            if next := cursor.children[ord(self.buffer[i])-97]:
                if next.isWord:
                    return True
                cursor = next
            else:
                return False
        for i in range(self.bIdx):
            if self.buffer[i]:
                if next := cursor.children[ord(self.buffer[i])-97]:
                    if next.isWord:
                        return True
                    cursor = next
                else:
                    return False        
        return False
