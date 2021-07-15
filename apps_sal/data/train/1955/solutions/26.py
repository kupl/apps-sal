class Solution:
    def __init__(self):
      self.roots = {}
      self.ranks = {}
      self.idx2chars = {}
      
    def find(self, idx) -> int:
      self.roots.setdefault(idx, idx)
      self.ranks.setdefault(idx, 1)
      self.idx2chars.setdefault(idx, [self.s[idx]])
      if self.roots[idx] != idx:
        self.roots[idx] = self.find(self.roots[idx])
      return self.roots[idx]
    
    def union(self, idx1, idx2) -> None:
      root1, root2 = self.find(idx1), self.find(idx2)
      if root1 != root2:
        if self.ranks[root2] < self.ranks[root1]:
          self.roots[root2] = root1
          self.idx2chars[root1].extend(self.idx2chars[root2])
        elif self.ranks[root2] > self.ranks[root1]:
          self.roots[root1] = root2
          self.idx2chars[root2].extend(self.idx2chars[root1])
        else:
          self.roots[root2] = root1
          self.idx2chars[root1].extend(self.idx2chars[root2])
          self.ranks[root1] += 1
    
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
      \"\"\"
      Union find, and for each union root, keep a queue of letters in sorted order. Then finally iterate over the string indices to re-build the string
      \"\"\"
      self.s = s
      for idx1, idx2 in pairs:
        root1, root2 = self.find(idx1), self.find(idx2)
        if root1 != root2:
          self.union(idx1, idx2)
      
      for idx in self.idx2chars:
        self.idx2chars[idx].sort(reverse=True)  # so we can pop the last
      
      # print(\"roots: \", self.roots)
      # print(\"idx2chars: \", self.idx2chars)
      
      ordered_chars = [''] * len(s)
      for idx in range(len(s)):
        root = self.find(idx)
        # print(\"idx, root: \", idx, root)
        ordered_chars[idx] = self.idx2chars[root].pop()
      
      return ''.join(ordered_chars)
