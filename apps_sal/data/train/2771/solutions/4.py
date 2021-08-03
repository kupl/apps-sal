li = [1, 1]
while len(li) != 1000:
    li.append(li[-li[-1]] + li[-li[-2]])


def hofstadter_Q(n): return li[n - 1]
