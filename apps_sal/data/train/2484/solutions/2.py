class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def diviser(n):
            if n == 4:
                return [1, 2]
            Result = [1]
            for i in range(2, n // 2):
                if n % i == 0:
                    Result.extend([int(i), int(n / i)])
            return Result

        def str_diviser(str3):
            Result = ['', str3]
            Result1 = diviser(len(str3))
            if len(Result1) > 0:
                for i in Result1:
                    div = str3[:i]
                    for j in range(i, len(str3), i):
                        if str3[j:(j + i)] != div:
                            break
                        if j == len(str3) - i:
                            Result.append(div)
            return Result
        a = str_diviser(str1)
        b = str_diviser(str2)
        if len(a) > len(b):
            a, b = b, a
        Cur = ''
        for i in a:
            if i in b and len(i) > len(Cur):
                Cur = i
        return Cur
