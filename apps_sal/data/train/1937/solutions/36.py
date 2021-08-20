class people:

    def __init__(self, name):
        self.name = name
        self.son = []
        self.alive = True


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = people(kingName)
        self.all_people = {}
        self.all_people[kingName] = self.king

    def birth(self, parentName: str, childName: str) -> None:
        self.all_people[childName] = people(childName)
        p = self.all_people[parentName]
        p.son.append(self.all_people[childName])

    def death(self, name: str) -> None:
        self.all_people[name].alive = False

    def getInheritanceOrder(self) -> List[str]:
        ans = []
        p = self.king
        stack = []
        while p or stack:
            if p.alive:
                ans.append(p.name)
            if p.son:
                for i in reversed(p.son[1:]):
                    stack.append(i)
                p = p.son[0]
            elif stack:
                p = stack.pop()
            else:
                p = None
        return ans
