def reverse_list(l):
    rs = []
    for n in l:
        print(n)
        rs.insert(0, n)
    return rs


r = reverse_list([1, 2, 3, 4])
print(r)
