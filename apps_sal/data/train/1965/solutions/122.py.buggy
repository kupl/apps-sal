class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        
        n_a={}
        n_b={}
        for e in edges:
            if e[0]==1 or e[0]==3:
                if e[1] not in n_a:
                    n_a[e[1]]=[]
                n_a[e[1]].append(e[2])
                if e[2] not in n_a:
                    n_a[e[2]]=[]
                n_a[e[2]].append(e[1])
            if e[0]==2 or e[0]==3:
                if e[1] not in n_b:
                    n_b[e[1]]=[]
                n_b[e[1]].append(e[2])
                if e[2] not in n_b:
                    n_b[e[2]]=[]
                n_b[e[2]].append(e[1])
                
        visited=set()
        l=list(n_b.keys())
        start=l[0]
        visited.add(start)
        q=[start]
        while q:
            actual=q[0]
            del q[0]
            if actual in n_a:
                for nb in n_a[actual]:
                    if nb not in visited:
                        visited.add(nb)
                        q.append(nb)
        if len(visited)!=n:
            return -1
        
        visited=set()
        l=list(n_b.keys())
        start=l[0]
        visited.add(start)
        q=[start]
        while q:
            actual=q[0]
            del q[0]
            if actual in n_b:
                for nb in n_b[actual]:
                    if nb not in visited:
                        visited.add(nb)
                        q.append(nb)
        if len(visited)!=n:
            return -1        

        
        
        
        
        
        
        parent_a={}
        parent_b={}
        for i in range(1,n+1):
            parent_a[i]=i
            parent_b[i]=i
            
        def find_a(x):
            if parent_a[x]!=x:
                parent_a[x]=find_a(parent_a[x])
            return parent_a[x]
        def find_b(x):
            if parent_b[x]!=x:
                parent_b[x]=find_b(parent_b[x])
            return parent_b[x]
        def union_a(x,y):
            x=find_a(x)
            y=find_a(y)
            if x!=y:
                parent_a[x]=y
                return 0
            else:
                return 1
        def union_b(x,y):
            x=find_b(x)
            y=find_b(y)
            if x!=y:
                parent_b[x]=y
                return 0
            else:
                return 1
        count=0
        for e in edges:
            if e[0]==3:
                u1=union_a(e[1],e[2])
                print(\"1\")
                u2=union_b(e[1],e[2])
                print(\"2\")
                if u1==u2 and u1==1:
                    count+=1
                    
        print(parent_a)
        print(parent_b)
        
        for e in edges:
            if e[0]==1:    
                u1=union_a(e[1],e[2])
                print(\"3\")
                if u1==1:
                    count+=1
            if e[0]==2:    
                u2=union_b(e[1],e[2])
                print(\"4\")
                if u2==1:
                    count+=1
        
        return count
                    
        
        
