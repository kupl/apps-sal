class Person:

    def __init__(self, name):
        self.children = []
        self.name = name
        self.isAlive = True


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.root = Person(kingName)
        self.persons = {kingName: self.root}

    def birth(self, parentName: str, childName: str) -> None:
        if parentName not in self.persons:
            return
        else:
            newChild = Person(childName)
            self.persons[parentName].children.append(newChild)
            self.persons[childName] = newChild

    def death(self, name: str) -> None:
        self.persons[name].isAlive = False

    def getInheritanceOrder(self) -> List[str]:
        ans = []

        def dfs(person):
            stack = [person]
            while len(stack) > 0:
                current = stack.pop()
                if current.isAlive:
                    ans.append(current.name)
                for child in current.children[::-1]:
                    stack.append(child)
        dfs(self.root)
        return ans
