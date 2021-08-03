class Solution:
    def sumByDigits(self, num: int) -> int:
        result, _n = 0, num
        while _n > 0:
            result += _n % 10
            _n = math.floor(_n / 10)
        return result

    def countLargestGroup(self, n: int) -> int:
        counter = collections.defaultdict(int)
        max_value = 0
        result = 0
        for i in range(1, n + 1):
            key = self.sumByDigits(i)
            counter[key] += 1
            if counter[key] > max_value:
                max_value = counter[key]
                result = 1
            elif counter[key] == max_value:
                result += 1
        return result
