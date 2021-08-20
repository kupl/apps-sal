def count_pairs_int(dif, n_max):
    _c = ((range(1, n_max)[i], range(1, n_max)[i + dif]) for i in range(0, len(range(1, n_max)) - dif))

    def v(x):
        _s = []
        for k in range(1, int(x ** 0.5) + 1):
            if x % k == 0:
                _s.append(k)
                _s.append(x / k)
        return len(set(_s))
    return len([i for i in _c if v(i[0]) == v(i[1])])
