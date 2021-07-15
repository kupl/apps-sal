class Person:
    def __init__(self, name, parent=None, children=[], isdead = False):
        self.name = name
        self.children = children
        self.parent = parent
        self.isdead = False

        

class ThroneInheritance:

    def __init__(self, kingName: str):
        self.kingName = kingName
        kingNode = Person(kingName, parent=\"kingfather\",children=[],isdead =False)
        self.Order = {kingName:kingNode}

        
    def birth(self, parentName: str, childName: str) -> None:
        self.Order[childName] = Person(childName,parent=parentName,children=[],isdead = False)
        self.Order[parentName].children.append(childName)
        

    def death(self, name: str) -> None:
        self.Order[name].isdead = True
        

    def getInheritanceOrder(self) -> List[str]:
        children_remain = {}
        for key,val in self.Order.items():
            
            children_remain[key] = len(self.Order[key].children)

        
        curOrder = []
        visited = {}

        self.Successor(self.kingName,curOrder,visited,children_remain)
        return curOrder

        
    def Successor(self,curName,curOrder,visited,children_remain):
        
        
        # print(self.Order[curName].children)
        # print(children_remain[curName])
        if self.Order[curName].isdead == False and curName not in visited:
            curOrder.append(curName)
            visited[curName] = 1

        if not self.Order[curName].children or children_remain[curName] == 0:
            if curName == self.kingName:
                return 
            else: 
                self.Successor(self.Order[curName].parent, curOrder,visited,children_remain)
        else:
            children_remain[curName] -= 1
            self.Successor(self.Order[curName].children[len(self.Order[curName].children)-children_remain[curName]-1], curOrder,visited,children_remain)
            
        return


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
