class Solution:
    def maxNumberOfFamilies(self, n: int, reserved: List[List[int]]) -> int:
        reserved.sort()
        result = 2 * n
        state = [1, 1, 1]
        for idx, (row, col) in enumerate(reserved):
            if idx > 0 and row != reserved[idx - 1][0]:
                if not state[0] or not state[2]:
                    result -= 1
                    if not any(state):
                        result -= 1
                state = [1, 1, 1]
            if col in range(2, 6):
                state[0] = 0
            if col in range(4, 8):
                state[1] = 0
            if col in range(6, 10):
                state[2] = 0
        if not state[0] or not state[2]:
            result -= 1
            if not any(state):
                result -= 1
        return result
