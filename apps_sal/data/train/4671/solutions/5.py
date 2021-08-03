def visit(ad_lst, i, fth=-1, path=[], visited=0):
    if i in path:
        return [], -1
    visited += 1
    path.append(i)
    for v in range(0, len(ad_lst[i])):
        if fth == ad_lst[i][v]:
            continue
        path2, v2 = visit(ad_lst, ad_lst[i][v], i, path)
        if len(path2) == 0:
            return [], -1
        path = path2
        visited += v2
    return path, visited


def isTree(ad_lst):
    for v in range(0, len(ad_lst)):
        path, visited = visit(ad_lst, v, -1, [], 0)
        if len(path) == 0:
            return False
        if visited == len(ad_lst):
            return True
    return False
