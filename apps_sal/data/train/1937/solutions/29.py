class Person(object):
    def __init__(self, name, p_name, live=True):
        self.name = name
        self.p_name = p_name
        self.live = live
        self.sibling = None
        self.first_child = None
        #######################################################
        # optimization 1: remember last_child for chain in O(1)
        #######################################################
        self.last_child = None


class ThroneInheritance:
    def __init__(self, kingName: str):
        self.curOrder = [kingName]
        self.curOrder_pos = {}
        self.inherit_pos = float('inf')
        self.person_map = {}
        self.person_map[kingName] = Person(kingName, None)

    def birth(self, parentName: str, childName: str) -> None:
        parent = self.person_map[parentName]
        children = parent.first_child
        # first child
        if children == None:
            parent.first_child = Person(childName, parentName)
            self.person_map[childName] = parent.first_child
            parent.last_child = parent.first_child
            #print('1 children:', parent.children.name, 'parent:', parent.children.p_name)
            #print('1 self.person_map=', self.person_map)
            # print('------')
        else:
            # add after last child
            parent.last_child.sibling = Person(childName, parentName)
            parent.last_child = parent.last_child.sibling
            self.person_map[childName] = parent.last_child
            #print('3 children:', children.name, 'parent:', children.p_name)
            #print('3 children.sibling:', children.sibling.name, 'parent:', children.sibling.p_name)
            #print('3 self.person_map=', self.person_map)
            # print('------')

        if parentName in self.curOrder_pos:
            self.inherit_pos = min(self.inherit_pos, self.curOrder_pos[parentName])

    def death(self, name: str) -> None:
        self.person_map[name].live = False

    def getInheritanceOrder(self) -> List[str]:
        # if x has no children or all of x's children are in curOrder:
        #    if x is the king return null
        #    else return Successor(x's parent, curOrder)
        # else return x's oldest child who's not in curOrder
        def successor(person_map, x, curOrder, curOrder_pos):
            p = person_map[x]
            # check if all p's children are in curOrder
            c = p.first_child
            o_c = None
            while c:
                #####################################
                # optimization 2: O(1) search in dict
                #####################################
                if c.name not in curOrder_pos:
                    o_c = c
                    break
                c = c.sibling

            if (not p.first_child) or (not o_c):
                return None if x == curOrder[0] else successor(person_map, p.p_name, curOrder, curOrder_pos)
            else:
                return o_c.name

        if self.inherit_pos != float('inf'):
            for i in range(self.inherit_pos + 1, len(self.curOrder)):
                del self.curOrder_pos[self.curOrder[i]]
            ###################################################################
            # optimization 3: only recalculate inheritence from parent impacted
            ###################################################################
            self.curOrder = self.curOrder[:self.inherit_pos + 1]

        nxt = successor(self.person_map, self.curOrder[-1], self.curOrder, self.curOrder_pos)
        while nxt:
            self.curOrder.append(nxt)
            self.curOrder_pos[nxt] = len(self.curOrder) - 1
            nxt = successor(self.person_map, nxt, self.curOrder, self.curOrder_pos)

        result = []
        for i, x in enumerate(self.curOrder):
            if self.person_map[x].live:
                result.append(x)

        self.inherit_pos = float('inf')
        return result


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
