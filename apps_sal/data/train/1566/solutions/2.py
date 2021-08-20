from sys import stdin, stdout
store = dict()


class node:

    def __init__(self, data):
        self.data = data
        self.parent = None
        self.rank = 0
        self.color = None


def makeset(data):
    new_node = node(data)
    new_node.parent = new_node
    store[data] = new_node


def union(data1, data2):
    node1 = store[data1]
    node2 = store[data2]
    parent1 = findset(node1)
    parent2 = findset(node2)
    if parent1.data == parent2.data:
        return
    if parent1.rank >= parent2.rank:
        parent1.rank += int(parent1.rank == parent2.rank)
        parent2.parent = parent1
    else:
        parent1.parent = parent2


def findset(new_node):
    parent = new_node.parent
    if new_node == parent:
        return new_node
    new_node.parent = findset(new_node.parent)
    return new_node.parent


def repre(data):
    return findset(store[data])


for _ in range(int(stdin.readline())):
    (n, q) = list(map(int, stdin.readline().split()))
    store = dict()
    different = []
    for i in range(1, n + 1):
        makeset(i)
    for i in range(q):
        (a, b, c) = list(map(int, stdin.readline().split()))
        if c == 0:
            union(a, b)
        else:
            different.append([a, b])
    ans = True
    for i in range(len(different)):
        ob1 = repre(different[i][0])
        ob2 = repre(different[i][1])
        if ob1.data == ob2.data:
            ans = 0
            break
        elif ob1.color == ob2.color and ob1.color != None:
            ans = 0
            break
        elif ob1.color == None and ob2.color == None:
            ob1.color = True
            ob2.color = not ob1.color
        elif ob1.color == None:
            ob1.color = not ob2.color
        elif ob2.color == None:
            ob2.color = not ob1.color
    if ans:
        stdout.write('yes\n')
    else:
        stdout.write('no\n')
