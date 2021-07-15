class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        q=collections.deque()
        
        def find_first_island():
            for i in range(len(A)):
                for j in range(len(A[0])):
                    if A[i][j]==1:
                        explore_island(i,j)
                        return
        def explore_island(r,c):
            if not 0<=r<len(A) or not 0<=c<len(A[r]) or A[r][c]==-1:
                return
            if A[r][c]==1:
                A[r][c]=-1
                explore_island(r+1,c)
                explore_island(r-1,c)
                explore_island(r,c+1)
                explore_island(r,c-1)
            elif A[r][c]==0:
                q.append((r,c,1))
        find_first_island()
        
        while q:
            cur_r,cur_c,cur_l=q.popleft()
            for x,y in (cur_r+1,cur_c),(cur_r-1,cur_c),(cur_r,cur_c+1),(cur_r,cur_c-1):
                if 0<=x<len(A) and 0<=y<len(A[0]):
                    if A[x][y]==1:
                        return cur_l
                    elif A[x][y]==0:
                        A[x][y]=-1
                        q.append((x,y,cur_l+1))

