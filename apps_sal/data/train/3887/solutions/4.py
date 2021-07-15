def pattern(n):
    lines = []
    for p in range(1,n):
        lines.append((str(p%10)*n).center(3*n-2))
    for p in range(1,n+1):
        lines.append(''.join([str(m%10) for m in range(1,n)] + [str(n%10) for m in range(n)] + [str(m%10) for m in range(1,n)[::-1]]))
    for p in range(n-1,0,-1):
        lines.append((str(p%10)*n).center(3*n-2))
    return '\n'.join(lines)
