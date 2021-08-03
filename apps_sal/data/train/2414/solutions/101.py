class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        total = 0
        for i in range(len(arr) - 2):
            for j in range(i + 1, len(arr) - 1):
                for z in range(j + 1, len(arr)):
                    new_arr = [arr[i], arr[j], arr[z]]
                    if (abs((new_arr[0] - new_arr[1])) <= a and (abs(new_arr[1] - new_arr[2])) <= b and (abs(new_arr[0] - new_arr[2])) <= c):
                        total += 1
        return total
