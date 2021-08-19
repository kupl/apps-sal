class Solution:

    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        seen = dict()
        is_fast_forwarded = False
        state_bitmap = 0
        for cell in cells:
            state_bitmap <<= 1
            state_bitmap = state_bitmap | cell
        while N > 0:
            if not is_fast_forwarded:
                if state_bitmap in seen:
                    N %= seen[state_bitmap] - N
                    is_fast_forwarded = True
                else:
                    seen[state_bitmap] = N
            if N > 0:
                N -= 1
                state_bitmap = self.nextDay(state_bitmap)
        ret = []
        for i in range(len(cells)):
            ret.append(state_bitmap & 1)
            state_bitmap = state_bitmap >> 1
        return reversed(ret)

    def nextDay(self, state_bitmap: int):
        state_bitmap = ~(state_bitmap << 1) ^ state_bitmap >> 1
        state_bitmap = state_bitmap & 126
        return state_bitmap
