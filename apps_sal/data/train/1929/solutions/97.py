class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = self.buildTrie(words)
        self.nodes = [self.trie]

    def buildTrie(self, words):
        trie = {}
        for word in words:
            curr = trie
            for char in word:
                if char not in curr:
                    curr[char] = {}
                curr = curr[char]
            curr['isWord'] = True
        return trie

    def query(self, letter: str) -> bool:
        found = False
        newNodes = [self.trie]
        for (i, node) in enumerate(self.nodes):
            if letter in node:
                if 'isWord' in node[letter]:
                    found = True
                    if len(list(node[letter].keys())) > 1:
                        newNodes.append(node[letter])
                else:
                    newNodes.append(node[letter])
        self.nodes = newNodes
        return found
