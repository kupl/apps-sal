def solve(a):
    for i in a:
        li = [i]
        while 1:
            if li[-1] % 3 == 0 and li[-1] // 3 in a:
                li.append(li[-1] // 3)
            elif li[-1] * 2 in a:
                li.append(li[-1] * 2)
            else:
                break
        if len(li) == len(a):
            return li
