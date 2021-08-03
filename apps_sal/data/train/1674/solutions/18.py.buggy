class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
      N = len(piles)
      @lru_cache(maxsize=None)
      def recurse(idx, m, alexTurn):
        # print(f\"RECURSE {idx} {m} {alexTurn}\")
        if idx + 2*m > N-1:

          return (sum(piles[idx:]), 0) if alexTurn else (0, sum(piles[idx:]))
          # return (0, 0)
        ops = []
        for x in range(1, 2*m+1):
          curNumStones = sum(piles[idx:idx+x])
          (nextA, nextL) = recurse(idx+x, max(m, x), not alexTurn)
          if alexTurn:
            ops.append((nextA+curNumStones, nextL))
          else:
            ops.append((nextA, nextL+curNumStones))
        [aScores, lScores] = list(zip(*ops)) 
        if alexTurn:
          return (max(aScores), max(lScores))
        else:
          return (min(aScores), max(lScores))
      return recurse(0, 1, True)[0]
    
    \"\"\"
    recurse(0, 1, True) -> 
      2 + recurse(1, 1, False) 
        recurse(1, 1, False) -> 
          9 + recurse(2, 1, True) 
          9 + 4 + recurse(3, 2, True)
      9 + recurse(2, 2, False)
          
    \"\"\"
