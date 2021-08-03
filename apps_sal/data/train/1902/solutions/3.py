class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:

        res = []

        def dfs(curr_num):
            if curr_num >= low and curr_num <= high:
                res.append(curr_num)
            elif curr_num > high:
                return

            if int(str(curr_num)[-1]) == 9:
                return
            dfs(curr_num * 10 + int(str(curr_num)[-1]) + 1)

        dfs(1)
        dfs(2)
        dfs(3)
        dfs(4)
        dfs(5)
        dfs(6)
        dfs(7)
        dfs(8)
        dfs(9)
        return sorted(res)
