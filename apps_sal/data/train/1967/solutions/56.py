class Solution:

    def splitIntoFibonacci(self, S: str) -> List[int]:
        result = []

        def getStarter():
            arr = []
            for i in range(1, len(S) - 1):
                for j in range(i + 1, len(S)):
                    (s1, s2) = (S[:i], S[i:j])
                    if s1[0] == '0' and len(s1) > 1 or (s2[0] == '0' and len(s2) > 1):
                        continue
                    arr.append((int(s1), int(s2), j))
            return arr

        def dfs(arr, start):
            if start == len(S) and len(arr) >= 3:
                result.append(arr)
                return True
            sum = arr[-2] + arr[-1]
            length = len(str(sum))
            nextNum = int(S[start:start + length])
            if 0 <= sum <= mx and nextNum == sum:
                return dfs(arr + [sum], start + length)
        arr = getStarter()
        mx = 2 ** 31 - 1
        for (num1, num2, start) in arr:
            if dfs([num1, num2], start):
                return result
        return []
