class ThroneInheritance:

    def __init__(self, kingName: str):
        self.people = {kingName: []}
        self.dead = dict()
        # storing the king name
        self.kn = kingName

    def birth(self, parentName: str, childName: str) -> None:
        if self.people.get(parentName, 0) != 0:
            self.people[parentName].append(childName)
        else:
            self.people[parentName] = [childName]

    def death(self, name: str) -> None:
        self.dead[name] = 1

    def getInheritanceOrder(self) -> List[str]:
        res = []

        # Defining DFS function for finding all parents and their children
        def dfs(curr, res):
            if self.dead.get(curr, 0) == 0:
                res.append(curr)
            if curr in list(self.people.keys()):
                for i in self.people[curr]:
                    dfs(i, res)

        dfs(self.kn, res)
        return res


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
