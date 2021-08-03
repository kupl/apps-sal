import collections

class Solution:
  def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
    swap_sets = [i for i in range(len(s))]
    
    for [a,b] in pairs:
      if not self.find(a,b,swap_sets):
        self.union(a,b, swap_sets)
        
    swap_sets = [self.root(s, swap_sets) for s in swap_sets]
    
    groups = collections.defaultdict(list)
    for i, charIndex in enumerate(swap_sets):
      groups[charIndex].append(i)
    
    for k,v in groups.items():
      chars = [s[i] for i in v]
      groups[k] = sorted(v), sorted(chars)
      
    subs = [v for k,v in groups.items()]
    newStr = ['' for i in range(len(s))]
    for indices, letters in subs:
      for i in range(len(indices)):
        newStr[indices[i]] = letters[i]
        
    return \"\".join(newStr)
      
      
  def union(self,a,b, roots):
    ra, rb = self.root(a, roots), self.root(b, roots)
    roots[rb] = ra
    
  def root(self,a, roots):
    while(roots[a] != a):
      roots[a] = roots[roots[a]]
      a = roots[a]
    return a
  
  def find(self,a,b, roots):
    return self.root(a, roots) == self.root(b, roots)
    
    
      
