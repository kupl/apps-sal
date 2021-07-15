class node:
    def __init__(self,name):
        self.data=name
        self.children=[]
class ThroneInheritance:

    def __init__(self, kingName: str):
        self.root=node(kingName)
        self.dic={}
        self.dic[kingName]=self.root
        self.dead={}
        

    def birth(self, parentName: str, childName: str) -> None:
        curr=self.dic[parentName]
        new=node(childName)
        curr.children.append(new)
        self.dic[childName]=new
    def death(self, name: str) -> None:
        self.dead[name]=True

    def getInheritanceOrder(self) -> List[str]:
        def dfs(node,ans):
            if node.data not in self.dead:
                ans.append(node.data)
            for child in node.children:
                dfs(child,ans)
        ans=[]
        dfs(self.root,ans)
        return ans


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()

