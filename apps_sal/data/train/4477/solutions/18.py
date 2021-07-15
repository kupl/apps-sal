def reverse_number(n):
    n = str(n)
    n = list(n)
    n.reverse()
    if n.count("-") > 0:
        n.pop()
        n.insert(0, "-") 
        
    a = str()
    for i in n:
        a += str(i)

    return int(a)
