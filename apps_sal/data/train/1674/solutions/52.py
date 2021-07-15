class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        @lru_cache(maxsize=None)
        def minimax(st, m, player):
            if st >= len(piles): return 0
            if player:
                return max([sum(piles[st:st+x]) + minimax(st+x, max(m,x), player^1) for x in range(1, 2*m+1)])
            else:
                return min([minimax(st+x, max(m,x), player^1) for x in range(1, 2*m+1)])
        return minimax(0, 1, 1)        

# [NOTE] Really good explanation here:
# https://leetcode.com/problems/stone-game-ii/discuss/345222/Python-Minimax-DP-solution
# The idea of minimax :
# If am the player 1 (whose winning sum we are trying to calculate), then I recurse on all possibilities and get the max.
# If am the player 2 (the opponent), then I try to minimize what P1 gets, and since we are not interested in what score P2 gets, we only calculate the min(all P1 next moves) and dont include the score P2 gets.
# Thanks to @douzigege for his comment which explains the minimax scenario specifically for this problem.

# if player == 1st player,
# gain = first x piles + minimax(..., 2nd player), where the gain is maximized
# if player == 2nd player,
# gain = 0 + minimax(..., 1st player), where the gain is minimized because the 2nd player tries to maximize this

# TLE for this input without@lru_cache
# [8270,7145,575,5156,5126,2905,8793,7817,5532,5726,7071,7730,5200,5369,5763,7148,8287,9449,7567,4850,1385,2135,1737,9511,8065,7063,8023,7729,7084,8407]

