def coin(n):
    return helper(n, '', [])


def helper(n, path, lst_of_ans):
    if n == 0:
        lst_of_ans.append(path)
        return lst_of_ans
    helper(n - 1, path + 'H', lst_of_ans)
    helper(n - 1, path + 'T', lst_of_ans)
    return lst_of_ans
