from collections import defaultdict

class UnionFind:
\tdef __init__(self):
\t\tself.parentsMap = {}\t# tracks the parents of nodes
\t\tself.rootLen = defaultdict(lambda:1)\t# tracks no. of nodes in it
\t
\tdef find(self, node: object)-> object:
\t\t\"returns the root node to the given (arg) node\"
\t\t# 1. creates parent-node of node if node not in parentsMap
\t\t# 2. loops through the parents of given node till the root 
\t\t# (the parent of given node is itself) not found and updates 
\t\t# the parent of the nodes and returns the root of node.
\t\tif node not in self.parentsMap:\tself.parentsMap[node]=node
\t\twhile node!=self.parentsMap[node]:
\t\t\ttemp = self.parentsMap[node]
\t\t\tself.parentsMap[node] = self.parentsMap[temp]
\t\t\tnode=temp
\t\treturn self.parentsMap[node]

\tdef union(self, node1: object, node2: object)-> None:
\t\t# finds the roots of the given nodes and points a lower len root 
\t\t# to other root
\t\tparent1 = self.find(node1)
\t\tparent2 = self.find(node2)
\t\tif parent1!=parent2:
\t\t\tif self.rootLen[parent1]<self.rootLen[parent2]:
\t\t\t\tself.parentsMap[parent1]=parent2
\t\t\t\tself.rootLen[parent2]+=self.rootLen[parent1]
\t\t\telse:
\t\t\t\tself.parentsMap[parent2]=parent1
\t\t\t\tself.rootLen[parent1]+=self.rootLen[parent2]

\tdef isConnected(self, node1: object, node2: object)-> bool:
\t\t# checks if roots of the given nodes are same and return true if 
\t\t# they are else false
\t\treturn self.find(node1)==self.find(node2)

        
class Solution:
    def minCostConnectPoints(self, A: List[List[int]]) -> int:
        dist = lambda a, b: sum(abs(i-j) for i,j in zip(a,b))
        n = len(A)
        # m = sum(i for i,j in A)/n, sum(j for i,j in A)/n
        u = UnionFind()
        res = 0
        d = []
        # A.sort(key = lambda x: dist(m, x))
        # print(A)
        
        for i in range(1, len(A)):
            for j in range(i):
                e1 = tuple(A[i])
                e2 = tuple(A[j])
                d.append((dist(e1, e2), e1, e2))
                # e1 = tuple(A[i])
                # print(e1, sorted(A, key = lambda x: dist(e1, x), reverse=1))
                # for e2 in map(tuple, sorted(A, key = lambda x: dist(e1, x), reverse=1)):
                    # if e1==e2:
                    #     continue
                    # if u.isConnected(e1, e2):
                    #     continue
                    # dis = dist(e1, e2)
                    # u.union(e1, e2)
                    # res+=dis
        
        for w, e1, e2 in sorted(d):
            # e2, w = e
            # print(e1, e2, w)
            if u.isConnected(e1, e2):
                continue
            u.union(e1, e2)
            res+=w
        
        return res
        
        
        
        
