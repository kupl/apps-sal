def count_by(x, n):
    i = 1
    count_list = []
    while i <= n:
        count_list.append(x * i)
        i += 1
    return count_list
