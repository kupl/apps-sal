def modified_sum(a, n):
    ans = 0
    for sq in a:
        ans = ans + sq ** n

    return ans - sum(a)
