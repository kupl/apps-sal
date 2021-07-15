# TODO: type solution here
class Node(object):
    def __init__(self, label):
        self.label = label
        self.par = self
        self.size = 1
        self.sum = 0
        self.seen = False


class DisjointSet(object):
    def __init__(self, n):
        self.n = n
        self.nodes = [Node(i) for i in range(n)]

    def find(self, u):
        if u != u.par:  # here we user path compression trick
            u.par = self.find(u.par)
        return u.par

    def unite(self, u, v):
        u, v = self.find(u), self.find(v)
        if u == v:  # u and v are in the same component
            return False

        # making v the vertex with bigger size
        if u.size > v.size:
            u, v = v, u

        # merging two components
        u.par = v

        # updating maximum size as size
        v.size += u.size
        v.sum += u.sum

        return True


n = int(input())
nums = [int(a) for a in input().split(" ")]
perm = [int(a) - 1 for a in input().split(" ")]
answers = []
current_answer = 0
dsu = DisjointSet(n)


def add(i, current_answer):
    node = dsu.nodes[i]
    node.seen = True
    node.sum = nums[i]
    if i > 0 and dsu.nodes[i - 1].seen:
        dsu.unite(node, dsu.nodes[i - 1])
    if i < n - 1 and dsu.nodes[i + 1].seen:
        dsu.unite(node, dsu.nodes[i + 1])

    parent = dsu.find(node)
    current_answer = max(current_answer, parent.sum)
    return current_answer


for i in range(n - 1, -1, -1):
    answers.append(current_answer)
    current_answer = add(perm[i], current_answer)

for i in range(n):
    print(answers[n - i - 1])

