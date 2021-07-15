class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        tree = dict()
        for i,j in edges:
            if i>j:
                i,j = j,i
            tree.setdefault(i-1,[]).append(j-1)
        q,time = [(0,1)],0
        while q and time <= t:
            tmp = []
            for node,prob in q:
                if node == target-1:
                    return 0 if time <t and node in tree else prob
                for n in tree.get(node,[]):
                    tmp.append((n,prob/len(tree[node])))
            q,time = tmp,time+1
        return 0
    
    


