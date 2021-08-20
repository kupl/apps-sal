from collections import defaultdict


class ListNode:

    def __init__(self, x, n=None):
        self.val = x
        self.next = n


class ThroneInheritance:

    def __init__(self, kingName: str):
        self.head = ListNode(kingName)
        self.d = defaultdict(list)
        self.dead_people = {'king': 0}

    def birth(self, parentName: str, childName: str) -> None:
        self.d[parentName].append(childName)
        self.dead_people[childName] = 0

    def death(self, name: str) -> None:
        self.dead_people[name] = 1

    def df(self, name):
        l = []
        if self.dead_people[name] == 0:
            l.append(name)
        for childs in self.d[name]:
            l = l + self.df(childs)
        return l

    def getInheritanceOrder(self) -> List[str]:
        return self.df('king')
