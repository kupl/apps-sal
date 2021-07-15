class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges1,edges2,edges3 = [],[],[]
        for t,u,v in edges:
            if t==1:
                E = edges1
            if t==2:
                E = edges2
            if t==3:
                E = edges3
            E.append((u,v))
        '''print(1, edges1)
        print(2, edges2)
        print(3, edges3)'''

        cnt = 0
        fathers = list(range(n+1))
    
        def find(fathers, v):
            if fathers[v]!=v:
                fathers[v]=find(fathers, fathers[v])
            return fathers[v]
        
        def union(fathers, a, b):
            rootA = find(fathers, a)
            rootB = find(fathers, b)
            if rootA != rootB:
                fathers[rootB] = rootA
                return True
            return False
        
        # type 3
        for u,v in edges3:
            if not union(fathers, u, v):
                cnt+=1
        
        #print(3, cnt)
        #print(fathers)
        def count(fathers, edges):
            cnt = 0
            for u,v in edges:
                if not union(fathers, u, v):
                    cnt+=1
            for i,v in enumerate(fathers):
                if i:
                    find(fathers, i)
            if len(set(fathers[1:]))>1:
                return -1
            return cnt
        # Alice
        a = count(fathers[:], edges1)
        #print('alice', a)
        if a==-1:
            return -1
        else:
            cnt+=a
        b = count(fathers[:], edges2)
        #print('bob', b)
        if b==-1:
            return -1
        else:
            cnt+=b
        return cnt
    

