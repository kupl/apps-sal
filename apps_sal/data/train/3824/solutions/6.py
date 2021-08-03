def find_spec_partition(n, k, com):
    if com == 'min':
        return [n - k + 1] + [1] * (k - 1)
    else:
        li, i = [1] * k, 0
        while sum(li) < n:
            li[i % k] += 1
            i += 1
        return li
