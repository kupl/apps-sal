import collections
import itertools
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        answer = [0] * len(puzzles)
        count = collections.Counter([frozenset(word) for word in words if len(set(word)) <= 7])
        
        for i, p in enumerate(puzzles):
            answer[i] = sum([count[frozenset(p[0] + \"\".join(s))]  for j in range(0, len(p)) for s in itertools.combinations(p[1:], j)])
            
        return answer
