def row_sum_odd_numbers(n):
    prev = 1
    ll = [y * [0] for y in range(1, n + 1)]
    for x in ll:
        for i in range(len(x)):
            x[i] = prev
            prev += 2
    return sum(ll[-1])
