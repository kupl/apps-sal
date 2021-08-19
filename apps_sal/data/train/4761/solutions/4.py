def search_k_from_end(linked_list, k):

    def rec(node, x):
        if not node:
            return x
        n = rec(node.next, x)
        return n if type(n) != int else n - 1 if n else node
    res = rec(linked_list.head, k - 1)
    if type(res) != int:
        return res.data
