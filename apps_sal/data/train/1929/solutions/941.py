class TrieNode:

    def __init__(self):
        self.children = {}
        self.leaf = False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = TrieNode()
        for word in words:
            node = self.trie
            for i in range(len(word)):
                c = word[i]
                if c not in node.children:
                    node.children[c] = TrieNode()
                node = node.children[c]
                if i == len(word) - 1:
                    node.leaf = True
        self.leads = []

    def query(self, letter: str) -> bool:
        new_leads = []
        result = False
        for lead in self.leads:
            if letter in lead.children:
                node = lead.children[letter]
                if node.leaf:
                    result = True
                new_leads.append(node)
        if letter in self.trie.children:
            if self.trie.children[letter].leaf:
                result = True
            new_leads.append(self.trie.children[letter])
        self.leads = new_leads
        return result
