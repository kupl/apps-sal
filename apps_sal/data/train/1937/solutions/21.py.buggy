

class Family:
    def __init__(self, parent):
        self.parent = parent
        self.children = []
    
    def __repr(self):
        return f\"parent: {self.parent}, children: {self.children}\"
        
class ThroneInheritance:

    def __init__(self, kingName: str):
        self.isdead = set()
        self.hierarchy = defaultdict(Family)
        self.hierarchy[kingName] = Family(None)

    def birth(self, parentName: str, childName: str) -> None:
        self.hierarchy[parentName].children.append(childName)
        self.hierarchy[childName] = Family(parentName)
        
    def death(self, name: str) -> None:
        self.isdead.add(name)

    def getInheritanceOrder(self) -> List[str]:            
        # def successor(x, curorder):
        #     if not self.hierarchy[x].children or all(child in curorder for child in self.hierarchy[x].children):
        #         if x == 'king': return None
        #         else: return successor(self.hierarchy[x].parent, curorder)
        #     else:
        #         for child in self.hierarchy[x].children:
        #             if child not in curorder:
        #                 return child
        # curorder = ['king']
        # curorder_set = ('king')
        # nxt = successor('king', curorder_set)
        # while nxt:
        #     curorder.append(nxt)
        #     nxt = successor(curorder[-1], curorder)
        
        i = 0
        curorderq, curorder = collections.deque(['king']), []
        while curorderq:
            curorder.append(curorderq.popleft())
            if self.hierarchy[curorder[-1]].children:
                for achild in self.hierarchy[curorder[-1]].children[::-1]:
                    curorderq.appendleft(achild)
        return [a for a in curorder if not a in self.isdead]

