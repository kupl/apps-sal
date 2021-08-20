class Solution:

    def circularPermutation(self, n: int, start: int) -> List[int]:
        original_list = [None for _ in range(1 << n)]
        original_list[0] = 0
        original_list[1] = 1
        for i in range(1, n):
            num_elements = 1 << i
            for j in range(num_elements):
                original_list[j] <<= 1
            for j in range(num_elements):
                original_list[num_elements + j] = original_list[num_elements - j - 1] + 1
        result_list = [None for _ in range(1 << n)]
        current = 0
        while original_list[current] != start:
            current += 1
        for i in range(1 << n):
            result_list[i] = original_list[(current + i) % (1 << n)]
        return result_list
