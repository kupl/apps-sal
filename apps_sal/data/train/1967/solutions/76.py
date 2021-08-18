class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        size = len(S)
        if size < 3:
            return []
        INT_MAX = (1 << 31) - 1

        def dfs(start, expect, prev, res):
            if start >= size:
                return len(res) >= 3
            for end in range(start, size):
                number = S[start:end + 1]
                if len(number) > 1 and number[0] == '0':
                    break
                num = int(number)
                if num > INT_MAX:
                    break
                if num == expect:
                    res.append(num)
                    if dfs(end + 1, expect + prev, expect, res):
                        return True
                    else:
                        res.pop()
                        break
                elif num > expect:
                    break
            return False
        for end in range(1, size):
            for mid in range(end):
                if S[0] == '0' and mid != 0:
                    continue
                if S[mid + 1] == '0' and end != mid + 1:
                    continue
                first = int(S[:mid + 1])
                second = int(S[mid + 1:end + 1])
                res = [first, second]
                if dfs(end + 1, second + first, second, res):
                    return res
        return []
