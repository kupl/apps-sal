class node:

    def __init__(self):
        self.child = [None] * 26
        self.end = False

    def insert(self, word):
        cur = self

        for i in range(len(word)):
            index = self.indexof(word[i])

            if cur.child[index] == None:
                cur.child[index] = node()

            cur = cur.child[index]

        cur.end = True

    def search(self, word):

        cur = self

        for w in word:
            index = self.indexof(w)

            cur = cur.child[index]

            if cur != None:
                if cur.end == True:
                    return True

            else:
                break

        return False

    def indexof(self, c):
        return ord(c) - ord('a')


class StreamChecker:

    def __init__(self, words: List[str]):
        self.words = words
        self.root = node()
        self.stack = collections.deque()

        for w in words:
            self.root.insert(w[::-1])

    def query(self, letter: str) -> bool:
        self.stack.appendleft(letter)

        return self.root.search(self.stack)
