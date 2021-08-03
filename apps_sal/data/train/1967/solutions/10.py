class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        # backtrack way
        n, ans = len(S), []

        def dfs(pos):
            if pos == n:
                return len(ans) >= 3

            num = 0
            for i in range(pos, n):
                if (S[pos] == '0' and i == pos) or S[pos] != '0':
                    num = num * 10 + ord(S[i]) - ord('0')
                    if num < 2 ** 31 - 1:
                        if len(ans) < 2 or (ans[-1] + ans[-2] == num):
                            ans.append(num)
                            if dfs(i + 1):
                                return True  # end early
                            ans.pop()
            return False
        dfs(0)
        return ans

# iteration
#         l = len(S)
#         m = 2 ** 31 - 1
#         for i in range(1, l):
#             if S[0] == '0' and i != 1:
#                 break

#             for j in range(i + 1, l):
#                 if S[i] == '0' and j != i + 1:
#                     break

#                 pre = int(S[:i])
#                 cur = int(S[i:j])
#                 res = [pre, cur]

#                 k = j
#                 while k < l:
#                     pre, cur = cur, pre + cur
#                     if cur <= m and int(S[k:k+len(str(cur))]) == cur:
#                         res.append(cur)
#                         k += len(str(cur))
#                     else:
#                         break
#                 if k == l and len(res) >= 3:
#                     return res
#         return []
