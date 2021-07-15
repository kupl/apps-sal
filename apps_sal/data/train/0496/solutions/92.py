class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        A = sorted(A)
        
        nums = set()
        move = 0
        prev = -1
        for i in range(len(A)):
            cur_num = A[i]
            if cur_num <= prev:
                cur_num = prev + 1
            while cur_num in nums:
                cur_num += 1
            nums.add(cur_num)
            move += (cur_num - A[i])
            prev = cur_num
            
            
        return move
