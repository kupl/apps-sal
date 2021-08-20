def complete_binary_tree(a):
    l = len(a)
    ans = [-1] * (l + 1)
    arr = a.copy()
    push_num(1, ans, arr)
    return ans[1:]


def push_num(idx, ans, a):
    if idx >= len(ans) or len(a) == 0:
        return
    else:
        push_num(idx * 2, ans, a)
        ans[idx] = a.pop(0)
        push_num(idx * 2 + 1, ans, a)
