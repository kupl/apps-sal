def positive_sum(arr):
    ans = []
    for n in list(arr):
        if n >= int(0):
           ans.append(n)
    return sum(ans)

