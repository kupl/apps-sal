from collections import deque


class Solution:
    def shiftingLetters(self, S: str, shifts: List[int]) -> str:
        offset = ord('a')
        wrap = 26
        current_shift = 0
        result = deque()
        for c, shift in reversed(list(zip(S, shifts))):
            current_shift = (current_shift + shift) % wrap
            after = chr(offset + (ord(c) + current_shift - offset) % wrap)
            result.append(after)
        return ''.join(reversed(result))
