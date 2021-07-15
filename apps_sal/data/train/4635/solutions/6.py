def create_octahedron(n):
    if n%2==0 or n<=1: return []
    m, y = n//2+1, []
    for j in range(m):
        x = [list(map(int,'0'*(m-i-1+(m-j-1))+'1'*(2*(j+i-m+1)+1)+'0'*(m-i-1+(m-j-1)))) if i>=m-j-1 else list(map(int,'0'*n)) for i in range(m)]
        y += [x+x[:-1][::-1]]
    return y+y[:-1][::-1]
