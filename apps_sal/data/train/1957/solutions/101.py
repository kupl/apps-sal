class valWrapper:
    def __init__(self, val, ind):
        self.val = val
        self.ind = ind

class Heap:
    def __init__(self, maxsize):
        self.size = 0
        self.heap = [None for i in range(maxsize)]
        self.ptr = {}
    
    def insert(self, key, val):
        ind = self.size
        v = valWrapper(val, ind)
        self.heap[ind] = v
        self.ptr[key] = v
        self.size += 1
        while(ind > 0 and self.heap[(ind-1)//2].val > self.heap[ind].val):
            self.heap[(ind-1)//2].ind, self.heap[ind].ind = ind, (ind-1)//2
            self.heap[(ind-1)//2], self.heap[ind] = self.heap[ind], self.heap[(ind-1)//2]
    
    def decrease_key(self, key, dec):
        self.ptr[key].val -= dec
        ind = self.ptr[key].ind
        while(ind > 0 and self.heap[(ind-1)//2].val > self.heap[ind].val):
            self.heap[(ind-1)//2].ind, self.heap[ind].ind = ind, (ind-1)//2
            self.heap[(ind-1)//2], self.heap[ind] = self.heap[ind], self.heap[(ind-1)//2]
            
    def extract(self):
        self.size -= 1
        minval = self.heap[0].val
        self.heap[self.size].ind = 0
        self.heap[0] = self.heap[self.size]
        ind = 0
        while(2*ind + 1 < self.size):
            swap_ind = 2 * ind + 1
            if 2 * ind + 2 < self.size and self.heap[2 * ind + 2].val < self.heap[2 * ind + 1].val:
                swap_ind += 1
            if self.heap[swap_ind].val < self.heap[ind].val:
                self.heap[swap_ind].ind, self.heap[ind].ind = ind, swap_ind
                self.heap[swap_ind], self.heap[ind] = self.heap[ind], self.heap[swap_ind]
                ind = swap_ind
            else:
                break
        return minval
                
class Solution:
    def get_neighbors(self, pos):
        neigh = []
        if pos[0] < self.M - 1:
            neigh.append([pos[0] + 1, pos[1]])
        if pos[0] > 0:
            neigh.append([pos[0] - 1, pos[1]])
        if pos[1] < self.N -1:
            neigh.append([pos[0], pos[1] + 1])
        if pos[1] > 0:
            neigh.append([pos[0], pos[1] - 1])
        # print(neigh)
        return neigh
    
    def argmin(self, dct):
        minval = float('inf')
        minkey = None
        for k, v in dct.items():
            if v < minval:
                minval = v
                minkey = k
        return minkey, minval
        
    def shortestPath3(self, grid: List[List[int]], k: int) -> int:
        self.M = len(grid)
        self.N = len(grid[0])
        dist = {(i, j , l) : float(\"inf\") for i in range(self.M) for j in range(self.N) for l in range(k+1)}
        V = set()
        for i in range(k+1):
            dist[(0, 0, i)] = 0
            
        for i in range(self.M * self.N * (k+1)):
            node, val = self.argmin(dist)
            # if node == None:
            #     print(dist)
            # print(i, node, val)
            if node == (self.M - 1, self.N -1, 0):
                return val
            if node == None:
                return -1
            V.add(node)
            dist.pop(node)
            neigh = self.get_neighbors(node[:2])
            cost = [grid[n[0]][n[1]] for n in neigh]
            neighk = [(n[0], n[1], l) for j, n in enumerate(neigh) for l in range(node[2] - cost[j] + 1)]
            neighk = [n for n in neighk if n not in V]
            for n in neighk:
                # print(n , node)
                dist[n] = min(dist[n], val + 1)
        return dist[(self.M-1, self.N-1, 0)]
    
    def shortestPath2(self, grid: List[List[int]], k: int) -> int:
        M = len(grid)
        N = len(grid[0])
        V = set()
        queue = [(0, 0, k, 0)]
        neighbors = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while len(queue) > 0:
            node = queue.pop(0)
            V.add(node[:3])
            if node[0] == M -1 and node[1] == N - 1:
                return node[3]
            for n in neighbors:
                xnew = n[0] + node[0]
                ynew = n[1] + node[1]
                if 0 <= xnew < M and 0 <= ynew < N and (node[2] - grid[xnew][ynew]) >= 0:
                    newnode = (xnew, ynew, node[2] - grid[xnew][ynew], node[3] + 1)
                    if newnode in V:
                        continue
                    queue.append(newnode)
        return -1
            
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        queue = deque()
        visited = set()
        queue.append((0, 0, k, 0))
        while queue:
            i, j, r, l = queue.popleft()
            if (i, j, r) in visited:
                continue
            visited.add((i,j,r))
            if grid[i][j] == 1:
                r -= 1
            if r < 0:
                continue
            if i == len(grid)-1 and j == len(grid[0])-1:
                return l
            neighbors = {(1,0), (0,1), (-1,0), (0,-1)}
            for n in neighbors:
                x,y=i+n[0],j+n[1]
                if 0<=x<len(grid) and 0<=y<len(grid[0]):
                    queue.append((x,y,r,l+1))
        return -1
                
                
