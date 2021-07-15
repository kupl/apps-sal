def prod_int_part(n):
    ans = []
    stack = [(n, 2, [])]
    while stack:
        v, m, divs = stack.pop()
        for i in range(m, int(v**0.5)+1):
            if v % i == 0:
                stack.append((v // i, i, divs + [i]))
                ans.append(divs + [i, v // i])
    return [len(ans), sorted(ans)[0]] if ans else [0, []]
