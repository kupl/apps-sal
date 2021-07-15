class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        v2edges={}
        red_edge_count=0
        blue_edge_count=0
        for typ,u,v in edges:
            v2edges.setdefault(v,[]).append((typ,u))
            v2edges.setdefault(u,[]).append((typ,v))
            if typ==1: red_edge_count+=1
            if typ==2: blue_edge_count+=1
        flagSet=set()
        def explore(allowedTypeSet,startVertex,flagEnabled=False):
            q=deque()
            visited=set()
            q.append(startVertex)
            visited.add(startVertex)
            if flagEnabled: flagSet.add(startVertex)
            while q:
                cur=q.popleft()
                for typ,dst in v2edges[cur]:
                    if typ in allowedTypeSet and dst not in visited:
                        q.append(dst)
                        visited.add(dst)
                        if flagEnabled: flagSet.add(dst)
            return visited
        
        if len(explore(set([1,3]),1))!=n: return -1
        if len(explore(set([2,3]),1))!=n: return -1
        
        cn=0
        cmpn=0
        v2gc={}
        gc_node_count=[]
        for v in range(1,n+1):
            if v in flagSet: continue
            cmpn+=1
            visited=explore(set([3]),v,True)
            if len(visited)>=2:
                for u in visited:
                    v2gc[u]=cn
                gc_node_count.append(len(visited))
                cn+=1
        
        green_edge_count=[0]*cn
        for typ,u,v in edges:
            if typ==3:
                ci=v2gc[u]
                green_edge_count[ci]+=1
        ans_red=max(0,red_edge_count-(cmpn-1))
        ans_blue=max(0,blue_edge_count-(cmpn-1))
        ans_green=sum(max(0,green_edge_count[ci]-(gc_node_count[ci]-1)) for ci in range(cn))
        ans=ans_red+ans_blue+ans_green
        return ans
