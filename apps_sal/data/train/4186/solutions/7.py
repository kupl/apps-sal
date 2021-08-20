def sum_of_threes(n):
    li = []
    while n >= 1:
        t = 0
        while 3 ** t <= n:
            t += 1
        n -= 3 ** (t - 1)
        li.append(f'3^{t - 1}')
    return ['+'.join(li), 'Impossible'][len(li) != len(set(li))]
