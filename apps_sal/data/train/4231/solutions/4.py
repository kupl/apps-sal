def a(n):
    if n<4: return ''
    n-=n%2
    l=2*n-1
    return '\n'.join((' '.join(['A']*(i+1)) if i*2==n else ''.join('A' if j in (0,i*2) else ' ' for j in range(i*2+1))).center(l) for i in range(n))
