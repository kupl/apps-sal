def tidyNumber(n):
    string_n = str(n)
    for (n1, n2) in zip(string_n, string_n[1:]):
        if n1 > n2:
            return False
    return True
