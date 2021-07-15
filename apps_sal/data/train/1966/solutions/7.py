class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        R, C = len(mat), len(mat[0])
        hist = [[0] * C for _ in range(R)]
        
        for r in range(R):
            for c in range(C):
                if mat[r][c]:
                    hist[r][c] = 1 if r == 0 else hist[r-1][c] + 1
        
        ret = 0
        for row in hist:
            all_stacks = []
            stack = []
            for num in row:
                if num > 0:
                    stack.append(num)
                elif stack:
                    all_stacks.append(stack[::])
                    stack = []
            if stack:
                all_stacks.append(stack)
            
            for stack in all_stacks:
                while stack:
                    last_h = stack[-1]
                    minsofar = last_h
                    for h in stack[::-1]:
                        minsofar = min(minsofar, h)
                        ret += minsofar
                    stack.pop()
            
        
        return ret

