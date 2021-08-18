class Solution:
    def divisorGame(self, N: int) -> bool:

        def divisors(N):
            if N == 1:
                return [1]

            res = []
            for n in range(1, int(N**0.5) + 1):
                if N % n == 0:
                    res.append(n)
            return res

        table = {
            1: False,
            2: True,
            3: False
        }

        def compute(i):
            if i in table:
                return table[i]

            divs = divisors(i)
            next_nums = [i - d for d in divs]

            for n in next_nums:
                status = compute(n)

                if status == False:
                    table[i] = True
                    return True
            table[i] = False
            return False

        return compute(N)
