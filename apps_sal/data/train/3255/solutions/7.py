def only_duplicates(a):
    b = []
    for j in range(0, len(a)):
        for i in range(j + 1, len(a)):
            if a[j] == a[i]:
                b.append(a[j])
    # zhao ti shen ye mei you yong
    a = list(a)

    def seclect(i):
        for j in b:
            if j == i:
                return i

    return ''.join(filter(seclect, a))
