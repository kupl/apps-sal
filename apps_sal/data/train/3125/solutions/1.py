def solve(n):
    answer = -1
    for D in range(1, max(int(n ** 0.5), 5)):
        R = (n - D ** 2) / (2 * D)
        if R.is_integer() and R > 0:
            answer = R ** 2
    return answer
