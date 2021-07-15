class TrieNode:
    def __init__(self):
        self.children = [None] *26
        self.count = 0

class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        self.root = TrieNode()
        for word in words:
            chars = sorted(set(list(word)))
            temp = \"\".join(chars)
            self.insert(temp)
        ans = []
        for puzzle in puzzles:
            ans.append(self.dfs(puzzle,self.root,False))
        return ans


    def dfs(self,puzzle,temp,collect = False):
        if not temp:
            return 0
        
        ans = temp.count if collect else 0
        
        for c in puzzle:
            index = ord(c) - ord('a')
            if temp.children[index]:
                ans += self.dfs(puzzle,temp.children[index], collect or c == puzzle[0])
        return ans
    
    def insert(self,word):
        temp = self.root
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if not temp.children[index]:
                temp.children[index] = TrieNode()
            temp = temp.children[index]
        temp.count += 1
        
