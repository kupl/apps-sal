#   多叉树--前序遍历
class Node:
    def __init__(self, name):
        self.val = name
        self.children = []
        self.alive = True

    def birth(self, child):
        self.children.append(child)

    def death(self):
        self.alive = False

    def check_alive(self):
        return self.alive


class ThroneInheritance:
    def __init__(self, kingName: str):
        #   天然是个树形结构
        #   为了生和死的快一些，需要能够通过名字直接找到各个节点
        self.king = Node(kingName)
        self.d = dict()
        self.d[kingName] = self.king

    def birth(self, parentName: str, childName: str) -> None:
        child = Node(childName)
        self.d[childName] = child

        self.d[parentName].birth(child)

    def death(self, name: str) -> None:
        self.d[name].death()

    def getInheritanceOrder(self) -> List[str]:
        #   前序遍历，只记录活着的
        rtv = []
        todo = []
        todo.append(self.king)
        while todo:
            t = todo.pop()
            if t.check_alive():
                rtv.append(t.val)
            for c in t.children[::-1]:
                todo.append(c)
        return rtv


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()
