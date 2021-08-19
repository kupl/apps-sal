class Solution:

    def splitIntoFibonacci(self, S):
        self.res = []

        def dfs(index, prev2, prev, count, cur_path):
            if index == len(S) and count >= 3:
                self.res = cur_path
                return
            for i in range(index, len(S)):
                x = int(S[index:i + 1])
                if count == 0:
                    dfs(i + 1, 0, x, count + 1, cur_path + [x])
                else:
                    if x > 1 << 31:
                        return False
                    if x == prev2 + prev or count == 1:
                        if dfs(i + 1, prev, x, count + 1, cur_path + [x]):
                            return True
                if x == 0:
                    break
        dfs(0, 0, 0, 0, [])
        return self.res
