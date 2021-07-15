def solve_eq(mat):
    determinant=lambda m:(m[0][0]*(m[1][1]*m[2][2]-m[2][1]*m[1][2]))-(m[0][1]*(m[1][0]*m[2][2]-m[2][0]*m[1][2]))+(m[0][2]*(m[1][0]*m[2][1]-m[1][1]*m[2][0]))
    d = determinant([i[:3] for i in mat])
    d1 = determinant([i[1:] for i in mat])
    d2 = determinant([[i[0],i[3],i[2]] for i in mat])
    d3 = determinant([i[:2] + [i[3]] for i in mat])
    return [d1/d,d2/d,d3/d]
