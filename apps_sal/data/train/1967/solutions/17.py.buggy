class Solution(object):
    def splitIntoFibonacci(self, S):
        \"\"\"
        :type S: str
        :rtype: List[int]
        \"\"\"
        def backtrack(cur, temp_state):
            if len(temp_state) >= 3 and cur == n:  # 退出条件
                self.res = temp_state[:]
                return
            for i in range(cur, n):
                if S[cur] == \"0\" and i > cur:  # 当数字以0开头时,应该跳过
                    return
                if int(S[cur: i+1]) > 2 ** 31 - 1 or int(S[cur: i+1]) < 0:  # 剪枝
                    continue
                if len(temp_state) < 2:
                    backtrack(i+1, temp_state + [int(S[cur: i+1])])
                else:
                    if int(S[cur: i+1]) == temp_state[-1] + temp_state[-2]:
                        backtrack(i+1, temp_state + [int(S[cur: i+1])])

        n = len(S)
        self.res = []
        backtrack(0, [])
        return self.res
        
