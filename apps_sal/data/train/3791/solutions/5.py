def moment_of_time_in_space(s):
    a = [int(x) for x in s if '1' <= x <= '9']
    (n, m) = (sum(a), len(s) - len(a))
    return [n < m, n == m, n > m]
