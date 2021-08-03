def first_non_consecutive(a):
    temp = [a[i] for i in range(len(a)) if i != 0 and a[i] != a[i - 1] + 1]
    return temp[0] if temp else None
