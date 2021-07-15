class Node:
    def __init__(self, val):
        self.val = val
        self.child = None
        self.next = None
        self.prev = None
        self.parent = None

class ThroneInheritance:

    def __init__(self, kingName: str):
        self.throne = Node(kingName)
        self.nodes = dict()
        self.nodes[kingName] = self.throne
    
    def birth(self, parentName: str, childName: str) -> None:
        node = self.nodes[parentName]
        if node.child:
            child = node.child
            while child.__next__ != None:
                child = child.__next__
            child.next = Node(childName)
            child.next.prev = child
            child.next.parent = node
            self.nodes[childName] = child.__next__
        else:
            node.child = Node(childName)
            node.child.parent = node
            self.nodes[childName] = node.child
        
    def death(self, name: str) -> None:
        
        del self.nodes[name]
            
            

    def getInheritanceOrder(self) -> List[str]:
        order = []
        if not self.throne:
            return None
        
        stack = [self.throne]
        while stack:
            curr = stack.pop()
            if curr.val in self.nodes:
                order.append(curr.val)
            
            if curr.__next__:
                stack.append(curr.__next__)
            if curr.child:
                stack.append(curr.child)
        return order
#[\"king\", \"andy\", \"matthew\", \"bob\", \"alex\", \"asha\", \"catherine\"]
# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

# [\"ThroneInheritance\",\"birth\",\"birth\",\"birth\",\"getInheritanceOrder\"]
# [[\"king\"],[\"king\",\"andy\"],[\"king\",\"bob\"],[\"andy\",\"matthew\"],[null]]

