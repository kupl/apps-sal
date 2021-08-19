class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = []  # variabel untuk menampung hasil perhitungan rumus
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                result.append((nums[i] - 1) * (nums[j] - 1))
        return max(result)  # mengambil nilai maximum dari rumus
