from collections import deque
class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]):
        graph = defaultdict(deque)
        group = Counter()
        visited = Counter()
        for u,v in dislikes:
            graph[u].append(v)
            graph[v].append(u)
        for j in range(1,n):
            if(visited[j]==0):
                stack = deque([j])
                while(stack):
                    ele = stack.pop()
                    for i in graph[ele]:
                        if(visited[i]==0):
                            stack.append(i)
                            visited[i] = 1
                            group[i] = 1-group[ele]
                        else:
                            if(group[i]!=1-group[ele]):
                                return False
        return True
