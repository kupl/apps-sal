# https://leetcode.com/problems/sum-of-distances-in-tree/
# https://github.com/tyqi11/leetcode/blob/master/834_Sum_of_Distances_in_Tree.java
class Solution:
    def sumOfDistancesInTree(self, N, edges):
        tree = collections.defaultdict(set)
        res = [0] * N
        count = [1] * N
        for i, j in edges:  # tree[i] contains all nodes connected to i.
            tree[i].add(j)
            tree[j].add(i)
        print(tree)

        def dfs(root, pre):  # Post order
            for i in tree[root]:
                if i != pre:
                    dfs(i, root)
                    count[root] += count[i]  # count[i]: # of nodes in subtree i.(+itself)
                    res[root] += res[i] + count[i]  # res[i]: sum of distance in subtree i.

        def dfs2(root, pre):  # Pre order
            for i in tree[root]:
                if i != pre:
                    res[i] = res[root] - count[i] + N - count[i]
                    dfs2(i, root)

        dfs(0, -1)
        dfs2(0, -1)
        # print(count)
        return res
