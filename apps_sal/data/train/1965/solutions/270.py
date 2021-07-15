class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        nei=[defaultdict(set),defaultdict(set),defaultdict(set)]
        count=[0,0,0]
        for i,j,k in edges:
            nei[i-1][j-1].add(k-1)
            nei[i-1][k-1].add(j-1)
            count[i-1]+=1
        def dfs(root,mark,seen,graph):
            seen[root]=mark
            for i in graph[root]:
                if not seen[i]:
                    dfs(i,mark,seen,graph)
        def cc(n,graph):
            cur=1
            seen=[0]*n
            for i in range(n):
                if not seen[i]:
                    dfs(i,cur,seen,graph)
                    cur+=1
            return (cur-1,seen)
        comp,group=cc(n,nei[2])
        res=count[2]-(n-comp)
        if comp==1:
            return res+count[0]+count[1]
        for i,j in list(nei[2].items()):
            nei[0][i]|=j
            nei[1][i]|=j
        comp1,group1=cc(n,nei[0])
        comp2,group2=cc(n,nei[1])
        if comp1!=1 or comp2!=1:
            return -1
        needed=(comp-1)*2
        return res+count[0]+count[1]-needed
        

