from collections import defaultdict

class Person:
    def __init__(self, name, parent):
        self.name = name
        self.is_alive = True
        self.parent = parent
        self.children = []

    def has_children(self):
        return True if len(self.children) > 0 else False

    def add_child(self, child):
        self.children.append(child)

class Order:
    def __init__(self):
        self.order = []
        self.names_set = set()

    def add(self, person):
        self.order.append(person)
        self.names_set.add(person.name)

    def not_in(self, persons):
        res = []
        for p in persons:
            if p.name not in self.names_set:
                res.append(p)
        return res



class ThroneInheritance:
    def __init__(self, kingName: str):
        self.family = defaultdict(Person)
        self.king = Person(kingName, None)
        self.family[kingName] = self.king

    def birth(self, parentName: str, childName: str) -> None:
        parent = self.family[parentName]
        new_child = Person(childName, parent)
        self.family[childName] = new_child
        self.family[parentName].add_child(new_child)


    def death(self, name: str) -> None:
        self.family[name].is_alive = False

    def getInheritanceOrder(self) -> 'List[str]':
        def successor(person, cur_order):
            children_not_in_order = cur_order.not_in(person.children)
            if not person.has_children() or not children_not_in_order:
                if person.parent is None:
                    return None
                else:
                    return successor(person.parent, cur_order)
            else:
                return children_not_in_order[0]

        order = Order()

        next_in_order = self.king
        while next_in_order:
            order.add(next_in_order)
            next_in_order = successor(next_in_order, order)

        res = []
        for p in order.order:
            if p.is_alive:
                res.append(p.name)

        return res
