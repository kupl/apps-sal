def solve(arr):
    ll = []
    for i in reversed(arr):
        if i not in ll:
            ll.insert(0, i)
    return ll
