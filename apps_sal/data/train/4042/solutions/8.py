def points(n):
    ct = (2*n+1)**2 # num of pts in lattice intersecting B_n(0)
    
    for x in range(-n,0): # x coords in (- , -) quadrant
        y = -n # inital y in (- , -) quadrant
        while x**2 + y**2 > n**2: #while outside B_n(0)
            ct -= 4 # use quadrant symmetry -  if its not in the (- , -) quad of B_n(0) its not in any quad.
            y += 1
    return ct
