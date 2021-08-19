from collections import deque


class Node:

    def __init__(self) -> object:
        self.children = dict()
        self.isEND = False
        self.fail = None


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, words):
        current_node = self.root
        for w in words:
            if current_node.children.get(w, None) is None:
                current_node.children[w] = Node()
            current_node = current_node.children[w]
        current_node.isEND = True

    def built_failover(self):
        q = deque()
        current = self.root
        for ch in self.root.children:
            self.root.children[ch].fail = self.root
            q.append(self.root.children[ch])
        while q:
            node = q.popleft()
            for ch in node.children:
                q.append(node.children[ch])
                failover = node.fail
                while True:
                    if failover is None:
                        node.children[ch].fail = self.root
                        break
                    if ch in failover.children:
                        node.children[ch].fail = failover.children[ch]
                        break
                    else:
                        failover = failover.fail


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for word in words:
            self.trie.insert(word)
        self.trie.built_failover()
        self.curr = self.trie.root

    def query(self, letter: str) -> bool:
        result = False
        while True:
            if letter in self.curr.children:
                self.curr = self.curr.children[letter]
                if self.curr.isEND:
                    result = True
                if self.curr.fail != None and self.curr.fail.isEND:
                    result = True
                break
            elif self.curr.fail == None:
                self.curr = self.trie.root
                break
            else:
                self.curr = self.curr.fail
        return result
