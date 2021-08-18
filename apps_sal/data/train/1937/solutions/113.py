class Person:
    def __init__(self, name: str, parent):
        self.name = name
        self.parent = parent
        self.alive = True
        self.children = []

    def add_kid(self, kid):
        self.children.append(kid)

    def kill(self):
        self.alive = False


class ThroneInheritance:
    def __init__(self, kingName: str):
        self.king = Person(kingName, None)
        self.person_dict = {kingName: self.king}

    def birth(self, parentName: str, childName: str) -> None:
        parent = self.person_dict[parentName]
        new_kid = Person(childName, parentName)
        self.person_dict[childName] = new_kid
        parent.add_kid(new_kid)

    def death(self, name: str) -> None:
        person = self.person_dict[name]
        person.kill()

    def getInheritanceOrder(self) -> List[str]:
        ans = []
        stack = [self.king]
        while stack:
            person = stack.pop()
            if person.alive:
                ans.append(person.name)
            if person.children:
                stack.extend(person.children[::-1])
        return ans
