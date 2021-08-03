class Node:
    def __init__(self, name):
        self.name = name
        self.next = dict()
        self.flag = False
        
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        head = dict()
        for f in folder:
            sub = f.split(\"/\")
            for i in range(1,len(sub)): # first element is empty string, skip
                            
                if i == 1: # first node
                    node = head.setdefault(sub[i], Node(sub[i]))
                else:
                    node = node.next.setdefault(sub[i], Node(sub[i]))
                    
                if i == len(sub)-1:
                    node.flag = True

        ret = list()
        # for k in head:
        #     # dfs
        #     stack = [(head[k], list())]
        #     while stack:
        #         node, chain = stack.pop()
        #         chain.append(node.name)
        #         if node.flag:
        #             ret.append(\"/\"+\"/\".join(chain))
        #         else:
        #             for k, next_node in node.next.items():
        #                 stack.append((next_node, list(chain)))
        
        
        def backtrack(node):
            if node.flag:
                return [[node.name]]
            
            ret = list()
            for k,v in node.next.items():
                l = backtrack(v)
                for i in range(len(l)):
                    l[i].append(node.name)
                ret.extend(l)
            return ret
                    
                
        ret = list()
        for k, v in head.items():
            # dfs
            for l in backtrack(v):
                ret.append(\"/\" + \"/\".join(l[::-1]))

        return ret
    
    
            
                    
                
                
                
                
        
