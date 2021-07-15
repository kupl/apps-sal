class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:

        seen = dict()
        is_fast_forwarded = False

        # step 1). convert the cells to bitmap
        state_bitmap = 0x0
        for cell in cells:
            state_bitmap <<= 1
            state_bitmap = (state_bitmap | cell)

        # step 2). run the simulation with hashmap
        while N > 0:
            if not is_fast_forwarded:
                if state_bitmap in seen:
                    # the length of the cycle is seen[state_key] - N 
                    N %= seen[state_bitmap] - N
                    is_fast_forwarded = True
                else:
                    seen[state_bitmap] = N
            # if there is still some steps remained,
            #   with or without the fast-forwarding.
            if N > 0:
                N -= 1
                state_bitmap = self.nextDay(state_bitmap)

        # step 3). convert the bitmap back to the state cells
        ret = []
        for i in range(len(cells)):
            ret.append(state_bitmap & 0x1)
            state_bitmap = state_bitmap >> 1

        return reversed(ret)


    def nextDay(self, state_bitmap: int):
        state_bitmap = ~ (state_bitmap << 1) ^ (state_bitmap >> 1)
        state_bitmap = state_bitmap & 0x7e  # set head and tail to zero
        return state_bitmap
