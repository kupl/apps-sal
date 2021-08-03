class ThroneInheritance:

    def __init__(self, kingName: str):
        dummy = TreeNode('', None)
        self.root = dummy
        self.lookup = {}
        
        self._addNode(kingName, dummy)

    def birth(self, parentName: str, childName: str) -> None:
        self._addNode(childName, self.lookup[parentName])

    def death(self, name: str) -> None:
        if name not in self.lookup:
            return
        
        node = self.lookup[name]
        #no children
        if node.firstChild.next.name == '':
            node.prev.next = node.next
            node.next.prev = node.prev
        else:
            firstChild = node.firstChild.next
            lastChild = node.lastChild.prev
            node.prev.next = firstChild
            firstChild.prev = node.prev
            node.next.prev = lastChild
            lastChild.next = node.next
            
        del node        

    def getInheritanceOrder(self) -> List[str]:
        res = []
        self._dfs(self.root, res)
        return res
        
    def _dfs(self, cur, res):
        if not cur:
            return
        
        if cur.name != '':
            res.append(cur.name)
            
        child = cur.firstChild
        while child:
            self._dfs(child, res)
            child = child.next
        
    def _addNode(self, name, parentNode):
        node = TreeNode(name, parentNode)
        self.lookup[name] = node
        
        prev = parentNode.lastChild.prev
        nxt = parentNode.lastChild
        node.prev = prev
        node.next = nxt
        prev.next = node
        nxt.prev = node
        
    def _print(self, name, node):
        print(name)
        while node:
            print(node.name + \"+\")
            node = node.next
        
class TreeNode:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.next = None
        self.prev = None
        self.firstChild = DummyNode()
        self.lastChild = DummyNode()
        
        self.firstChild.next = self.lastChild
        self.lastChild.prev = self.firstChild
        
class DummyNode:
    def __init__(self):
        self.name = ''
        self.next = None
        self.prev = None
        self.firstChild = None
        self.lastChild = None

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
