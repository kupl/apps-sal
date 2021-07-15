class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        ea=[set() for _ in range(n)]
        eb=[set() for _ in range(n)]
        ec=[set() for _ in range(n)]
        nodea=set()
        nodeb=set()
        nodec=set()
        na, nb, nc= 0, 0, 0
        for edge in edges:
            if edge[0]==1:
                ea[edge[1]-1].add(edge[2]-1)
                ea[edge[2]-1].add(edge[1]-1)
                na+=1
            if edge[0]==2:
                eb[edge[1]-1].add(edge[2]-1)
                eb[edge[2]-1].add(edge[1]-1)
                nb+=1
            if edge[0]==3:
                ea[edge[1]-1].add(edge[2]-1)
                ea[edge[2]-1].add(edge[1]-1)
                eb[edge[1]-1].add(edge[2]-1)
                eb[edge[2]-1].add(edge[1]-1)
                ec[edge[1]-1].add(edge[2]-1)
                ec[edge[2]-1].add(edge[1]-1)
                nodec.add(edge[2]-1)
                nodec.add(edge[1]-1)
                nc+=1
        nodea.add(0)
        q=[0]
        p=0
        while p<len(q):
            for node in ea[q[p]]:
                if node in nodea:
                    continue
                else:
                    q.append(node)
                    nodea.add(node)
            p+=1
        if len(q)<n:
            return -1
        nodeb.add(0)
        q=[0]
        p=0
        while p<len(q):
            for node in eb[q[p]]:
                if node in nodeb:
                    continue
                else:
                    q.append(node)
                    nodeb.add(node)
            p+=1
        if len(q)<n:
            return -1
        n1=len(nodec)
        n2=0
        while len(nodec):
            n2+=1
            q=[nodec.pop()]
            p=0
            while p<len(q):
                for node in ec[q[p]]:
                    if node in nodec:
                        q.append(node)
                        nodec.remove(node)
                p+=1
        return len(edges)-(2*n-2-n1+n2)
