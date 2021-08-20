from collections import deque


class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        p = self.root
        for c in word:
            if c not in p.children:
                p.children[c] = TrieNode()
            p = p.children[c]
        p.is_word = True
        return p


class Solution:

    def removeSubfolders(self, folder: List[str]) -> List[str]:
        if folder is None or not folder:
            return []
        trie = Trie()
        for f in folder:
            trie.insert(f)
        ret = []
        queue = deque([(trie.root, '')])
        while queue:
            (p, acc) = queue.popleft()
            if p.is_word:
                ret.append(acc)
            for letter in p.children:
                if p.is_word and letter == '/':
                    continue
                queue.append((p.children[letter], acc + letter))
        return ret
