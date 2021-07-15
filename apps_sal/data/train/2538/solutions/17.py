class Solution:
    def countLargestGroup(self, n: int) -> int:
        sums = {}
        max_len = 0
        for num in range(1, n + 1):
            digits = str(num)
            sum = 0
            if len(digits) > max_len:
                max_len = len(digits)
            for char in digits:
                sum = sum + int(char)
            
            arr = [sum, num]
            
            arr = [sum, num]
            
            if sum in sums:
                sums[sum].extend([arr])
            else:
                sums[sum] = [arr]
        
        sorted_sums = sorted(sums, reverse=True, key = lambda x: len(sums.get(x)))
        max_len = len(sums.get(sorted_sums[0]))
        count = 0
        for key in sorted_sums:
            items = sums.get(key)
            if len(items) != max_len:
                break
            else:
                count = count + 1
        
        return count
