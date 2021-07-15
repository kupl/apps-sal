def get_neighbourhood(n_type, mat, coord):
    x, y = coord[0], coord[1]
    if x<0 or y<0 or x>=len(mat) or y>=len(mat[0]):
        return []
    val = [(x-1, y), (x, y-1), (x, y+1), (x+1, y)]
    if n_type == 'moore':
        val += [(x-1, y-1), (x-1, y+1), (x+1, y-1), (x+1, y+1)]
    return [mat[a[0]][a[1]] for a in val if a[0]>=0 and a[0]<len(mat) and a[1]>=0 and a[1]<len(mat[0])]

