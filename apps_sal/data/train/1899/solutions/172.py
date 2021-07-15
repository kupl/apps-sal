class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        def trace_island(A, start_i, start_j, second, edges):
            queue = collections.deque()
            queue.append((start_i, start_j))
            
            while queue:
                i, j = queue.popleft()
                isedge = False
                for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1), (0, 0)]:
                    if  0 <= di+i < len(A) and 0<= dj+j < len(A[0]) and A[di+i][dj+j] == 1:
                        if second:
                            A[di+i][dj+j] = 2
                        else:
                            A[di+i][dj+j] = -1

                        if not (di ==0 and dj==0):
                            queue.append((di+i, dj+j))
                    else:
                        isedge = True
                if isedge and not second:
                    edges.append((i,j))
            
        
        outedge = []
        second = False
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    trace_island(A, i, j, second, outedge)
                    print(A)
                    second = True
        output = 0
        while(outedge):
            temp = []
            for i, j in outedge:
                for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                    if  0 <= di+i < len(A) and 0<= dj+j < len(A[0]) and A[di+i][dj+j] != -1:
                        if A[di+i][dj+j] == 2:
                            return output
                        temp.append((di+i, dj+j))
                        A[di+i][dj+j] = -1
            outedge = temp
            output += 1

    
                
                    
                    
        

