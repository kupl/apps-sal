class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:

        def dfs(index, res, s):
            # print(res)
            if index == len(s) and len(res) >= 3:
                return True
            num = 0
            for i in range(index, len(s)):
                num = num * 10 + (ord(s[i]) - ord('0'))
                if num > 2**31 - 1:
                    break
                if len(res) > 2 and (num > res[-1] + res[-2]):
                    break
                if s[index] == '0' and i > index:
                    break
                if len(res) < 2 or (res[-1] + res[-2] == num):
                    res.append(num)
                    if dfs(i + 1, res, s):
                        return True
                    res.pop()

            return False
        result = []
        dfs(0, result, S)
        return result
