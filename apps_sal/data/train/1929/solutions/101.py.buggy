class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:

    def __init__(self):
        \"\"\"
        Initialize your data structure here.
        \"\"\"
        self.root = TrieNode()
        
    def insert_suffix(self, word, node):
        if word == '':
            return
        if word[0] not in node.children:
            node.children[word[0]] = TrieNode()
        self.insert_suffix(word[1:], node.children[word[0]])

    def insert(self, word):
        \"\"\"
        Inserts a word into the trie.
        \"\"\"
        word = word + '$'
        self.insert_suffix(word, self.root)
        
    def print_subtree(self, node):
        print(list(node.children.keys()))
        for child in node.children.values():
            self.print_subtree(child)
            
    def __str__(self):
        self.print_subtree(self.root)

class StreamChecker:

    def __init__(self, words):
        self.Trie = Trie()
        for word in words:
            self.Trie.insert(word)
        # print(self.Trie)
        self.matches = [self.Trie.root] # a list of nodes which represent terminal letters of all the currently active partial matches
        
    def query(self, letter):
        found_match = False
        extended_matches = [self.Trie.root]
        for match in self.matches:
            if letter in match.children:
                new_match = match.children[letter]
                if '$' in new_match.children:
                    found_match = True
                extended_matches.append(new_match)
        self.matches = extended_matches
        # print(self.matches)
        return found_match
            
      
