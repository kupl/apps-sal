def pattern(n):
    if n <= 0:
        return ''
    li = []
    for i in range(1, n):
        temp = [str(i % 10)if j == i - 1 else ' 'for j in range(n - 1)]
        li.append("".join(temp) + " " + "".join(temp[::-1]))
    return "\n".join(["\n".join(li), str(n % 10).center(n * 2 - 1), "\n".join(li[::-1])])
