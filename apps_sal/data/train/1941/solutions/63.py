class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:

        class TrieNode():
            def __init__(self):
                self.children = collections.defaultdict(TrieNode)
                self.word_inds = []

            def add(self, x, word_ind):
                if x:
                    self.children[x[0]].add(x[1:], word_ind)
                else:
                    self.word_inds.append(word_ind)

        root = TrieNode()

        for ind, word in enumerate(words):
            root.add(sorted(set(word)), ind)

        counts = []
        for puzzle in puzzles:
            nodes = [root]
            for letter in sorted(puzzle):
                new_nodes = []
                for node in nodes:
                    if letter in node.children:
                        new_nodes.append(node.children[letter])
                nodes += new_nodes
            count = 0
            for node in nodes:
                for word_ind in node.word_inds:
                    if puzzle[0] in words[word_ind]:
                        count += 1
            counts.append(count)

        return counts
