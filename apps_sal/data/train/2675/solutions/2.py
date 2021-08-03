def bad_apples(apples):
    bad = (x if x else y for x, y in apples if (not x) ^ (not y))
    result, flag = [], True
    for x in apples:
        if all(x):
            result.append(x)
        elif any(x):
            if flag:
                try:
                    result.append([next(bad), next(bad)])
                except StopIteration:
                    pass
            flag = not flag
    return result
