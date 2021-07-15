class Solution:
    def countLargestGroup(self, n: int) -> int:
        def sumDigits(n):
            if n < 10: return n
            sum = 0
            while n:
                sum += n % 10
                n //= 10
            return sum
        cnt = [0 for i in range(37)] 
        max_size, max_cnt = 0, 0
        while n:
            cnt[sumDigits(n)] += 1
            if max_size < cnt[sumDigits(n)]:
                max_size = cnt[sumDigits(n)]
                max_cnt = 1
            else:
                max_cnt += max_size == cnt[sumDigits(n)]
            n -= 1
        return max_cnt    
