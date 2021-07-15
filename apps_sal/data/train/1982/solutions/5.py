class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        if N==1 or not dislikes:
            return True
        x={i:[] for i in range(1,N+1)}
        for i,j in dislikes:
            x[i].append(j)
            x[j].append(i)
        colour=[-1]*N
        for i in range(1,N+1):
            if colour[i-1]==-1:
                colour[i-1]=0
                q=[i]
                while q:
                    node=q.pop()
                    for j in x[node]:
                        if colour[node-1]==colour[j-1]:
                            return False
                        if colour[j-1]==-1:
                            colour[j-1]=colour[node-1]^1
                            q.append(j)
        return True
