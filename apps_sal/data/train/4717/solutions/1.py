def pattern(n):
    lines = []
    for c in range(1,n+1):
      s = (' ' * (n-c)) + ''.join([str(s)[-1] for s in range(1,c+1)])
      lines += [s + s[::-1][1:]]
    lines += lines[::-1][1:]
    return '\n'.join(str(x) for x in lines)

