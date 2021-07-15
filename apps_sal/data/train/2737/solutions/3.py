def near_flatten(a):
    li = []
    def do(a):
        for i in a:
            li.append(i if all(isinstance(k, int) for k in i) else do(i))
    do(a)
    return sorted([i for i in li if i])
