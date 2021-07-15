def expression_matter(a, b, c):
    mass = [a,b,c]
    return max([(mass[0]+mass[1])*mass[2],(mass[0]+mass[1])+mass[2],mass[0]*(mass[1]+mass[2]),(mass[0]*mass[1])*mass[2]])
