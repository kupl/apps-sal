class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        nums = [num + 1, num + 2]
        pair = (1, num+1)
        seen = collections.defaultdict(bool)

        for i,num in enumerate(nums):
            for j in range(1, int(sqrt(num))+1):
                if seen[j]:
                    continue

                if num % j == 0:
                    seen[num // j] = True
                    if abs(pair[0] - pair[1]) > abs(j - num // j):
                        pair = (j, num // j)
        return pair
