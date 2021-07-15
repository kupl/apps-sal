class Solution:
    def divisorGame(self, N: int) -> bool:
      return win_game(N)
    
from functools import lru_cache
@lru_cache(maxsize=None)
def win_game(N):
  return any(not win_game(N-x) for x in range(1,N) if N % x == 0)
