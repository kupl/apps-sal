def reverse_letter(string):
    a = []
    a[:] = string
    a.reverse()
    b = []
    c = ''
    let = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for s in a:
        if s in let:
            b.append(s)
    for ele in b:
        c += ele
    return c
