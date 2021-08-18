class Node:
    def __init__(self,):
        self.children = [None] * 26
        self.terminal = False


class Trie:
    def __init__(self,):
        self.root = Node()
        self.size = 0

    def get_index(self, x):
        return ord(x) - ord('a')

    def insert(self, input_str):
        curr = self.root
        for x in input_str:
            c = self.get_index(x)
            if curr.children[c] is not None:
                curr = curr.children[c]
            else:
                curr.children[c] = Node()
                curr = curr.children[c]
        curr.terminal = True

    def search(self, input_str):
        curr = self.root
        for x in input_str:
            c = self.get_index(x)
            if curr.children[c] is not None:
                curr = curr.children[c]
                if curr.terminal:
                    return True
            else:
                return False
        return curr.terminal


class StreamChecker:
    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            self.trie.insert(word[::-1])
        self.request_string = ''

    def query(self, letter: str) -> bool:
        '''
        ab ba aaab abab baa

        ba ab 

        '''
        self.request_string = letter + self.request_string
        result = self.trie.search(self.request_string)

        return result
