class Node:
    def __init__(self, name):
        self.name = name
        self.prev = None
        self.next = None
        
class ThroneInheritance:

    def __init__(self, kingName: str):
        self.deaths = set()
        self.deaths.add(\"\")
        self.nameToNode = {}
        self.head = Node(\"\")
        self.tail = Node(\"\")
        self.kingName = kingName
        
        king = Node(kingName)
        self.head.next = king
        king.next = self.tail
        self.tail.prev = king
        king.prev = self.head
        
        self.nameToNode[kingName] = {\"node\": king, \"children\": [], \"parent\": None}
        
    def birth(self, parentName: str, childName: str) -> None:
        parent = self.nameToNode[parentName]
        prev_node = parent[\"node\"]
        if parent[\"children\"]:
            prev_node = parent[\"children\"][-1]
            while self.nameToNode[prev_node.name][\"children\"]:
                prev_node = self.nameToNode[prev_node.name][\"children\"][-1]
        
        c_node = Node(childName)
        parent[\"children\"].append(c_node)
        self.nameToNode[childName] = {\"node\":c_node, \"children\":[], \"parent\": parent[\"node\"]}
        
        post_node = prev_node.next
        prev_node.next = c_node
        c_node.next = post_node
        post_node.prev = c_node
        c_node.prev = prev_node
        

    def death(self, name: str) -> None:
        self.deaths.add(name)

    def getInheritanceOrder(self) -> List[str]:
        node = self.nameToNode[self.kingName][\"node\"]
        res = []
        while node:
            if node.name not in self.deaths:
                res.append(node.name)
            node = node.next
        return res
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
