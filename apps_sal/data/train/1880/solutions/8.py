class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        def next(state):
            return tuple(1 if i > 0 and i < len(state) - 1 and state[i - 1] == state[i + 1] else 0 for i in range(len(state)))

        seen = {}
        state = tuple(cells)

        i = 0
        remaining = 0
        while i < N:
            if state in seen:
                cycle = i - seen[state]
                remaining = (N - i) % cycle
                break
            seen[state] = i
            state = next(state)
            i += 1

        while remaining > 0:
            state = next(state)
            remaining -= 1

        return state
