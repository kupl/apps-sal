import bisect
import math
from pprint import pformat as pf
from pprint import pprint as pp
import sys
sys.setrecursionlimit(10 ** 7)


class Tree:
    """
    node id starts from 1
    """
    DUMMY = 0

    def __init__(self, num_node, node_values):
        self.node_values = [-1] + node_values
        self.edges = [None] * (num_node + 1)
        for (i, _) in enumerate(self.edges):
            self.edges[i] = set()
        self.seq = [self.DUMMY] * num_node
        self.dp = [math.inf] * (num_node + 1)
        self.dp[0] = -1 * math.inf
        self.ans = [0] * (num_node + 1)

    def node_values(self, node_values):
        self.node_values = [-1] + node_values

    def make_edge(self, a, b):
        self.edges[a].add(b)
        self.edges[b].add(a)

    def dps(self, node_id, prev=0, depth=0):
        value = self.node_values[node_id]
        key = bisect.bisect_left(self.dp, value)
        old_value = self.dp[key]
        self.dp[key] = value
        self.ans[node_id] = max(key, self.ans[prev])
        for to in self.edges[node_id]:
            if to == prev:
                continue
            self.dps(to, node_id, depth + 1)
        self.dp[key] = old_value


def __starting_point():
    num_node = int(input())
    node_values = list(map(int, input().split()))
    tree = Tree(num_node, node_values)
    for i in range(num_node - 1):
        (frm, to) = list(map(int, input().split()))
        tree.make_edge(frm, to)
    tree.dps(1)
    for a in tree.ans[1:]:
        print(a)


__starting_point()
