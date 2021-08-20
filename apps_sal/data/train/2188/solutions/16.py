from collections import defaultdict
LVL = 18


def pattern_repr(x):
    rep = [1 if int(x) % 2 else 0 for x in x]
    return [0] * (LVL - len(rep)) + rep


class Node:

    def __init__(self, key, node_id=0):
        self.key = key
        self.node_id = node_id
        self.left = None
        self.right = None


class CodeforcesTask713ASolution:

    def __init__(self):
        self.result = ''
        self.t = 0
        self.queries = []

    def read_input(self):
        self.t = int(input())
        for _ in range(self.t):
            self.queries.append(input().split(' '))

    def process_task(self):
        res = []
        root = Node(0, 1)
        node_id = 2
        treesol = False
        if treesol:
            for query in self.queries:
                if query[0] in '+-':
                    pattern = pattern_repr(query[1])
                    current = root
                    while pattern:
                        if pattern[0]:
                            if current.right:
                                current = current.right
                            else:
                                current.right = Node(0, node_id)
                                current = current.right
                                node_id += 1
                        elif current.left:
                            current = current.left
                        else:
                            current.left = Node(0, node_id)
                            current = current.left
                            node_id += 1
                        pattern = pattern[1:]
                    current.key += 1 if query[0] == '+' else -1
                else:
                    pattern = [int(x) for x in '0' * (LVL - len(query[1])) + query[1]]
                    current = root
                    while pattern:
                        if pattern[0]:
                            if current.right:
                                current = current.right
                            else:
                                current = Node(0)
                                pattern = []
                        elif current.left:
                            current = current.left
                        else:
                            current = Node(0)
                            pattern = []
                        pattern = pattern[1:]
                    res.append(current.key)
        else:
            counts = defaultdict(int)
            for query in self.queries:
                if query[0] in '+-':
                    pattern = '0' * (LVL - len(query[1])) + ''.join(('1' if int(x) % 2 else '0' for x in query[1]))
                    counts[pattern] += 1 if query[0] == '+' else -1
                else:
                    pattern = '0' * (LVL - len(query[1])) + query[1]
                    res.append(counts[pattern])
        self.result = '\n'.join([str(x) for x in res])

    def get_result(self):
        return self.result


def __starting_point():
    Solution = CodeforcesTask713ASolution()
    Solution.read_input()
    Solution.process_task()
    print(Solution.get_result())


__starting_point()
