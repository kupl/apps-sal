class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        # generate the Gray code for `n` bits
        gray_code = [1, 0]
        for i in range(1, n):
            next_gray_code = []
            increase = 1 << i
            for num in gray_code:
                next_gray_code.append(num + increase)
            for num in reversed(gray_code):
                next_gray_code.append(num)
            gray_code = next_gray_code
        # then rotate the list backwards until `start` is at the beginning
        idx = gray_code.index(start)
        return gray_code[idx:] + gray_code[:idx]
