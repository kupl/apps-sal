class Solution:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        stack = [0]
        larger_index = [-1] * len(A)
        
        for i in range(1, len(A)):
            while stack and A[i] >= A[stack[-1]]:
                stack.pop()
            if stack:
                larger_index[i] = stack[-1]
            stack.append(i)
        
        print(larger_index)
        idx, swap = len(larger_index), -1
        for i in range(len(larger_index) - 1, -1, -1):
            if larger_index[i] == -1:
                continue
            if larger_index[i] > swap or (larger_index[i] == swap and A[i] >= A[idx]):
                val = A[larger_index[i]]
                idx = i
                swap = larger_index[i]
        if swap != -1:
            A[swap], A[idx] = A[idx], A[swap]
        return A
            
            

