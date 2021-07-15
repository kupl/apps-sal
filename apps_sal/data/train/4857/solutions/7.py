def square_up(n):
    """
    Codewars 练习题: Array - squareUp b!
    :param n:
    :return:
    """
    ans = []
    for i in range(1, n + 1):
        for k in range(n - i):
            ans.append(0)
        for j in range(i, 0, -1):
            ans.append(j)
    return ans
