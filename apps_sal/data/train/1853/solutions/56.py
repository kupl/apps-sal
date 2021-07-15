class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        storage = [[30000 if i != j else 0 for i in range(n) ] for j in range(n)]
        for edge in edges:
            storage[edge[0]][edge[1]] = edge[2]
            storage[edge[1]][edge[0]] = edge[2]
        
        #FloydWarshallAPSP
        for k in range(0, n):
            for i in range(0, n):
                for j in range(0, n):
                    currD = storage[i][j]
                    toK = storage[i][k]
                    fromK = storage[k][j]
                    storage[i][j] = min(storage[i][j], toK + fromK)
                    
        print(\"storage\", storage)
        
        #Process to get answer
        numCities = [0 for i in range(n)]
        currLowestCity = 0
        currLowestCount = 200
        for i in range(0, n):
            count = 0
            for j in range(0, n):
                if storage[j][i] <= distanceThreshold:
                    count += 1
            if count <= currLowestCount:
                currLowestCity = i
                currLowestCount = count
        
        return currLowestCity

