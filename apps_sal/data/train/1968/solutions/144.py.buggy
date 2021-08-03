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

            for i in range(1,len(sub)):
                if i == 1:
                    if sub[i] not in head:
                        head[sub[i]] = Node(sub[i])
                    node =  head[sub[i]]
                    if i == len(sub)-1:
                        node.flag = True
                elif i == len(sub) -1:
                    if sub[i] not in node.next:
                        node.next[sub[i]] = Node(sub[i])
                    node.next[sub[i]].flag = True
                else:
                    if sub[i] not in node.next:
                        node.next[sub[i]] = Node(sub[i])
                    node = node.next[sub[i]]
                    
            
        ret = list()
        # print(head)
        for k in head:
            # dfs
            stack = [(head[k], list())]
            while stack:
                node, chain = stack.pop()
                chain.append(node.name)
                if node.flag:
                    ret.append(\"/\"+\"/\".join(chain))
                else:
                    for k, next_node in node.next.items():
                        stack.append((next_node, list(chain)))
                        
            
            
            
            
            
        return ret
            
                    
                
                
                
                
        
