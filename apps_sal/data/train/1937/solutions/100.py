class Person:
    def __init__(self, name):
        self.name = name
        self.alive = True
        self.children = []


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = Person(kingName)
        self.name_person_map = {kingName: self.king}

    def birth(self, parentName: str, childName: str) -> None:
        parent = self.name_person_map[parentName]
        child = Person(childName)
        parent.children.append(child)
        self.name_person_map[childName] = child

    def death(self, name: str) -> None:
        person = self.name_person_map[name]
        person.alive = False

    def getInheritanceOrder(self) -> List[str]:
        res = []
        self.preorder_dfs(self.king, res)
        return res

    def preorder_dfs(self, person, res):
        if person.alive:
            res.append(person.name)
        for child in person.children:
            self.preorder_dfs(child, res)
