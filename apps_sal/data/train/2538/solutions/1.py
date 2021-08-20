class Solution:

    def countLargestGroup(self, n: int) -> int:
        if n < 10:
            return n
        counter = [0] * 37
        sumCount = {0: 0}
        i = 1
        while i <= n:
            (quotient, reminder) = divmod(i, 10)
            sumCount[i] = reminder + sumCount[quotient]
            counter[sumCount[i]] += 1
            i += 1
        return counter.count(max(counter))
