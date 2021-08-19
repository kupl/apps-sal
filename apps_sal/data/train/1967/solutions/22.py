class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        n = len(S)
        ans = []

        def dfs(position):
            # means at end of string
            if position == n:
                return True if len(ans) > 2 else False

            num = 0

            for i in range(position, n):
                # build number from string
                num = num * 10 + ord(S[i]) - ord('0')

                # check for integer overflow
                if num >= 2**31:
                    break

                # check len and last elem in ans + 2nd to last elem in ans = num
                if len(ans) < 2 or ans[-1] + ans[-2] == num:
                    # add to ans, start of backtracking portion
                    ans.append(num)
                    # recurse on next index, if true return true
                    if dfs(i + 1):
                        return True
                    # pop recently add num from ans
                    ans.pop()

                # check for trailing/leading 0s and i == position
                if i == position and S[i] == '0':
                    return False

            return False
        # call
        dfs(0)
        return ans
