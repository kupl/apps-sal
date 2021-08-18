class Solution:
    '''
    Intuition
    Add Type3 first, then check Type 1 and Type 2.

    Explanation
    Go through all edges of type 3 (Alice and Bob)
    If not necessary to add, increment res.
    Otherwith increment e1 and e2.

    Go through all edges of type 1 (Alice)
    If not necessary to add, increment res.
    Otherwith increment e1.

    Go through all edges of type 2 (Bob)
    If not necessary to add, increment res.
    Otherwith increment e2.

    If Alice's'graph is connected, e1 == n - 1 should valid.
    If Bob's graph is connected, e2 == n - 1 should valid.
    In this case we return res,
    otherwise return -1.

    Complexity
    Time O(E), if union find with compression and rank
    Space O(E)

    '''

    def maxNumEdgesToRemove(self, n, edges):
        def find(i):
            if i != root[i]:
                root[i] = find(root[i])
            return root[i]

        def uni(x, y):
            x, y = find(x), find(y)
            if x == y:
                return 0
            root[x] = y
            return 1

        res = e1 = e2 = 0

        root = list(range(n + 1))
        for t, i, j in edges:
            if t == 3:
                if uni(i, j):
                    e1 += 1
                    e2 += 1
                else:
                    res += 1
        root0 = root[:]

        for t, i, j in edges:
            if t == 1:
                if uni(i, j):
                    e1 += 1
                else:
                    res += 1

        root = root0
        for t, i, j in edges:
            if t == 2:
                if uni(i, j):
                    e2 += 1
                else:
                    res += 1

        return res if e1 == e2 == n - 1 else -1
