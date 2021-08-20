def smallest_integer(m):
    return (lambda s: min({n + 1 for n in s if -1 <= n} - s))(set(sum(m, [-1])))
