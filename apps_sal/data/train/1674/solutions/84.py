class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        self.piles = piles
        self.memo = {}
        return self.minimax(0, 1, True)

    def minimax(self, start: int, M: int, is_player_1: bool) -> int:
        if start >= len(self.piles):
            return 0
        if (start, M, is_player_1) in self.memo:
            return self.memo[(start, M, is_player_1)]
        if is_player_1:
            output = max([
                sum(self.piles[start:start + x]) + self.minimax(start + x, max(x, M), False)
                for x in range(1, min(2 * M, len(self.piles)) + 1)
            ])
        else:
            output = min([
                self.minimax(start + x, max(x, M), True)
                for x in range(1, min(2 * M, len(self.piles)) + 1)
            ])
        self.memo[(start, M, is_player_1)] = output
        return output
