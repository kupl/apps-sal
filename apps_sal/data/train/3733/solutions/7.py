def arithmetic_sequence_elements(a, r, n):
    out = [str(a)]
    for i in range(n - 1):
        a += r
        out.append(str(a))
    
    return ", ".join(out)

