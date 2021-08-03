class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        dq = deque([(0, 0, 0, 1)])
        seen = {(0, 0, 0, 1)}
        steps = 0
        
        while dq:
            length = len(dq)
            
            for _ in range(length):
                r0, c0, r1, c1 = dq.popleft()
                if r0==r1==M-1 and c0==N-2 and c1==N-1:
                    return steps
                
                if r0==r1:
                    # horizontal
                    # rotate clockwise
                    if r0+1<M and not grid[r0+1][c0] and not grid[r1+1][c1] \\
                        and (r0, c0, r0+1, c0) not in seen:
                        seen.add((r0, c0, r0+1, c0))
                        dq.append((r0, c0, r0+1, c0))
                elif c0==c1:
                    # vertical
                    # rotate counter clockwise
                    if c1+1<N and not grid[r0][c0+1] and not grid[r1][c1+1] \\
                        and (r0, c0, r0, c0+1) not in seen:
                        seen.add((r0, c0, r0, c0+1))
                        dq.append((r0, c0, r0, c0+1))
                
                # 1. move right
                if c1+1<N and not grid[r0][c0+1] and not grid[r1][c1+1] \\
                    and (r0, c0+1, r1, c1+1) not in seen:
                    seen.add((r0, c0+1, r1, c1+1))
                    dq.append((r0, c0+1, r1, c1+1))
                    
                # 2. move down
                if r1+1<M and not grid[r0+1][c0] and not grid[r1+1][c1] \\
                    and (r0+1, c0, r1+1, c1) not in seen:
                    seen.add((r0+1, c0, r1+1, c1))
                    dq.append((r0+1, c0, r1+1, c1))
                    
            steps += 1
        return -1
