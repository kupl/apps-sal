class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        '''
        all of them are connected so the only possibility that is invalid is that its only type 1 or only type2 -> -1
        the rest is 0 - 
        find cycles ?
        find if we have type3, we dont need type1 or type2 -> check if we have enough type 3 
        then we check type 1 and 2 
        UNION FIND !!!
        '''
        root = [k for k in range(n+1)]
       
        def find(i):
            if i != root[i]:
                root[i] = find(root[i])
            return root[i]
        
        def union(val1,val2):
            val1,val2 = find(val1),find(val2)
            if val1 == val2:
                return 1
            root[val1] = val2
            return 0
        
        remove = t1 = t2 = 0
        for ty,fr,to in edges:
            if ty == 3:
                if union(fr,to):
                    remove += 1
                else:
                    t1 +=1
                    t2 +=1

        temp_root = root[:]
        for ty,fr,to in edges:
            if ty == 1:
                if union(fr,to):
                    remove += 1
                else:
                    t1 += 1
                        
        root = temp_root
        for ty,fr,to in edges:       
            if ty == 2:
                if union(fr,to):
                    remove += 1
                else:
                    t2 += 1
               
        return remove if (t1 == t2 == n-1) else -1

