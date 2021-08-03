\"\"\"
There are 2 pieces of information to memo: 1. Alice's maximum score, 2. Bob's maximum score. Combine them into a tuple and store it in a dict, the key of which is (current index, m).
We will start from the piles[index], and compute the cumulative sum all the way up to piles[index+2*m].
Then we recursively call the DP function with the new index and m. After trying all the possible ways, take the maximum value, and store it in the dict.

\"\"\"
class Solution:
    def stoneGameII(self, piles):
        d = {} # (idx, m): (Alice's score, Bob's score)
        def DP(idx, m):
            if idx>=len(piles):
                return (0,0)
            if (idx,m) in d:
                return d[(idx,m)] # Memo!
            s, ans, oppo = 0, 0, 0
            for i in range(idx, idx+2*m): # try all the possible sum
                if i>=len(piles):
                    break
                s += piles[i]
                dp_ans = DP(i+1, max(m, i-idx+1)) # fetch the result from subproblem
                if s+dp_ans[1]>ans:
                    ans = s+dp_ans[1] # [1] is the real Alice's score from the next subproblem
                    oppo = dp_ans[0] # [0] is Bob's score
            d[(idx,m)] = (ans, oppo) # store the information
            return (ans, oppo)

        ans = DP(0, 1)
        return ans[0]
