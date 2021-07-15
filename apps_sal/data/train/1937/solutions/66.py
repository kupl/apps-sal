class ThroneInheritance:

    def __init__(self, kingName: str):
        self.family = OrderedDict()
        self.family[kingName] = OrderedDict()
        self.parentChildrenDictMap = dict()
        self.parentChildrenDictMap[kingName] = self.family[kingName]
        self.dead = set()

    def birth(self, parentName: str, childName: str) -> None:
        # import pprint
        # pprint.pprint(self.family)
        # pprint.pprint(self.parentChildrenDictMap)
        if parentName not in self.parentChildrenDictMap:
            raise Exception('No parent found')
        children = self.parentChildrenDictMap[parentName]
        if childName in children:
            raise Exception('Child already exists')
        children[childName] = OrderedDict()
        self.parentChildrenDictMap[childName] = children[childName]
                 

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        ans = []
        def dfs(root):
            for parent, children in list(root.items()):
                if parent not in self.dead:
                    ans.append(parent)
                dfs(root[parent])
        dfs(self.family)
        return ans
            
    
    


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

