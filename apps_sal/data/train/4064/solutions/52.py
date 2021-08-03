def count_by(x, n):
    ans = []
    i = x
    count = 0
    while count < n:
        ans.append(i)
        i += x
        count += 1
    return ans
