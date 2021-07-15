class Node():
    def __init__(self,val):
        self.val=val
        self.children=[]
    
    def add_edge(self,child):
        self.children.append(child)
        child.parent=self
    
    def count(self):
        res_num=0
        res_val=0
        for c in self.children:
            temp_num,temp_val=c.count()
            res_num+=temp_num
            res_val+=temp_val
        self.res_num=res_num
        self.res_val=res_val
        return res_num+1,res_val+(res_num+1)
    
    def dist(self,res,p_num,p_val):
        res[self.val]=p_val+self.res_val
        for c in self.children:
            c.dist(res,p_num+self.res_num-c.res_num,(p_val+self.res_val-c.res_val-c.res_num-1)+(p_num+self.res_num-c.res_num))
        
    
    
class STree():
    def __init__(self,n,edges):
        self.nodes=[Node(i) for i in range(n)]
        self.res=[0 for i in range(n)]
        edges_dic=collections.defaultdict(list)
        for i in range(len(edges)):
            edges_dic[edges[i][0]].append(edges[i][1])
            edges_dic[edges[i][1]].append(edges[i][0])
        queue=[0]
        visited=[0 for i in range(n)]
        visited[0]=1
        while(queue):
            current=queue.pop(0)
            for c in edges_dic[current]:
                if visited[c]==0:
                    visited[c]=1
                    self.nodes[current].add_edge(self.nodes[c])
                    queue.append(c)
    
    def count(self):
        self.nodes[0].count()
    
    def dist(self):
        self.nodes[0].dist(self.res,0,0)
        return self.res
    
    

class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        t=STree(N,edges)
        t.count()
        return t.dist()
        

