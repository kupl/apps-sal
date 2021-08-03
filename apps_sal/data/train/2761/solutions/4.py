def length_of_line(pts):
    return f'{sum((a-b)**2 for a,b in zip(*pts))**.5:.2f}'
