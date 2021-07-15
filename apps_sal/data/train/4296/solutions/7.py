def largest(n,xs):
    lst = sorted(xs)
    new = []
    for i in range(n):
        new.append(lst[-i-1])
    return sorted(new)

