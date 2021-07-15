from collections import defaultdict
class Solution:
    def possibleBipartition(self, n, dislikes):
        self.visited = {}
        self.graph = defaultdict(list)
        for p1, p2 in dislikes:
            self.graph[p1].append(p2)
            self.graph[p2].append(p1)
        for personId in range(len(self.graph)):
            if personId not in self.visited:
                if not self.dfs(personId, 1): #color the personId 1
                    return False
        return True
        
    def dfs(self, personId, color): #color personId as color. all its dislikers as opposite color. return true if possible. false otherwise
        if personId in self.visited:
            return self.visited[personId]==color

        self.visited[personId] = color
        for neighbor in self.graph[personId]:            
            if not self.dfs(neighbor, -color): #color the neighbor -1*color. opposite to personId
                return False
        return True

