class Solution:
    def binaryGap(self, n: int) -> int:
        binary_string = bin(n)[2:]
        # The binary string has to begin with a 1, if n is a positive integer.

        left, right, current_distance, global_max = 0, 1, 1, 0

        print(binary_string)
        while right <= len(binary_string) - 1:
            print(left, right, current_distance, global_max)
            if binary_string[right] == '0':
                right += 1
                current_distance += 1
            else:
                global_max = max(global_max, current_distance)
                left = right
                right += 1
                current_distance = 1

        return global_max
