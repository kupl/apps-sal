def find(n):
    mof3 = [i for i in range(3, n + 1, 3)]
    mof5 = [i for i in range(5, n + 1, 5)]
    mof3.extend(mof5)
    all_num_to_n = set(sorted(mof3))
    return sum(all_num_to_n)
