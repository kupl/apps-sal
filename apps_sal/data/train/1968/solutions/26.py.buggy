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

                # first node
                if i == 1:
                    node = head.setdefault(sub[i], Node(sub[i]))
                # not first node
                else:
                    print
                    node = node.next.setdefault(sub[i], Node(sub[i]))
                    # print(node.next)
                    
                if i == len(sub)-1:
                    node.flag = True
                # if 1 < 1 < len(sub)-1:
                #     node = next_node


        print(head) 
        ret = list()
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
            
                    
                
                
                
                
        
