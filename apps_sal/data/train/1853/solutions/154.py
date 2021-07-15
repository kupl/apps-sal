class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        if n == 0:
            return 0
        
        if len(edges) == 0:
            return 0
        
        dict1 = collections.defaultdict(list)
        dict2 = collections.defaultdict(list)
        for edge in edges:
            dict1[edge[0]].append((edge[1],edge[2]))
            dict1[edge[1]].append((edge[0],edge[2]))
    
        self.dict1 = dict1
        self.distanceThreshold = distanceThreshold
        tempres = []
        for i in range(n):
            temp = self.neighbours(i)
            tempres.append((temp,i))
        print(tempres)
        return sorted(tempres, key = lambda x:([x[0]],[-x[1]]))[0][1] 
    
    def neighbours(self,i):    
            
            heap = [(0,i)]
            d = {}

            while heap:

                distance , node = heappop(heap)

                if node in d:
                    continue

                if node != i:
                    d[node] = distance

                for nei,w in self.dict1[node]:
                    
                    if nei in d:
                        continue

                    if distance+w <= self.distanceThreshold:
                        heappush(heap,(distance+w,nei))
                
            return len(d)
        
        
        
        
        
        
                             
        
            
        
        

