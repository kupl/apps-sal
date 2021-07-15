def subsets_parity(n,k):
    string_set = "{:02b}".format(n)
    length = len(string_set)
    string_subset = "{:02b}".format(k).zfill(length)
    for i in range(0, length):
        if not int(string_set[i]) and int(string_subset[i]):
            return "EVEN"
            break
    else:
        return "ODD"
