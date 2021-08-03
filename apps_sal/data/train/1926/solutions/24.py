class Solution:
    def closestDivisors(self, num: int) -> List[int]:
        n = num + 1
        m = num + 2
        size = int(math.sqrt(m) + 1)
        holder = m
        result = [0] * 2

        for i in range(1, size):
            if n % i == 0:
                temp = n // i
                if holder > abs(temp - i):
                    holder = abs(temp - i)
                    result[0] = temp
                    result[1] = i
            if m % i == 0:
                temp = m // i
                if holder > abs(temp - i):
                    holder = abs(temp - i)
                    result[0] = temp
                    result[1] = i
        return result
