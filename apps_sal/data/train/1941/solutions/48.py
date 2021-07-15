import collections
class Node(object):
    def __init__(self):
        self.dic = collections.defaultdict(Node)
        self.counter = 0
        
    def insert(self, word):
        if not word:
            return
        node = self.dic[word[0]]
        for ind in range(1, len(word)):
            node = node.dic[word[ind]]
        node.counter += 1
        
            
class Solution(object):
    def findNumOfValidWords(self, words, puzzles):
        \"\"\"
        :type words: List[str]
        :type puzzles: List[str]
        :rtype: List[int]
        \"\"\"
        
        def dfs(puzzle, i, node):
            if i == len(puzzle):
                self.count += node.counter
                return 
            
            if puzzle[i] == self.initial:
                if puzzle[i] not in node.dic:
                    return
                dfs(puzzle, i + 1, node.dic[puzzle[i]])
                
            else:
                dfs(puzzle, i + 1, node)
                if puzzle[i] not in node.dic:
                    return
                dfs(puzzle, i + 1, node.dic[puzzle[i]])
        
        trie = Node()
        for word in words:
            word = ''.join(sorted(set(word)))
            trie.insert(word)
        
        
        final = [0 for _ in range(len(puzzles))]
        for ind in range(len(puzzles)):
            self.initial = puzzles[ind][0]
            self.count = 0
            puzzle = ''.join(sorted(set(puzzles[ind])))
            dfs(puzzle, 0, trie)
            final[ind] = self.count
            
        return final
