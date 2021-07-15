class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        ans = []
        dfs(S, [], ans)
        return ans[0] if ans else []

        
def dfs(S, temp, ans):
    # print(S)
    # print(temp)
    if len(temp) >= 3 and not is_valid_fibonacci(temp):
        return
    if S == \"\":
        if len(temp) >= 3:
            ans.append(temp.copy())
        return 
    for i in range(1, len(S) + 1):
        sub_str = S[:i]
        rest_str = S[i:]
        # '01' is not allowed
        if sub_str.startswith('0') and len(sub_str) != 1:
            continue
        num = int(sub_str)
        # 0 <= F[i] <= 2^31 - 1, (that is, each integer fits a 32-bit signed integer type);
        if num < 0 or num > 2 ** 31 - 1:
            continue
        # print(sub_str)
        # print(rest_str)
        temp.append(num)
        dfs(rest_str, temp, ans)
        temp.pop()
        
def is_valid_fibonacci(items):
    # check last 3 elements
    return items[-1] == items[-2] + items[-3]
        
