import math
def get_score(x,y):
    P = '6 13 4 18 1 20 5 12 9 14 11 8 16 7 19 3 17 2 15 10 6'
    C = [(0,'DB'),(12.7,'SB'),(31.8,''),(198,'T'),(214,''),(324,'D'),(340,'X')]
    r, phi = math.sqrt(x*x+y*y), 180*math.atan2(y, x)/math.pi
    phi += [0,360][phi < 0]
    p = [p for i, p in enumerate(P.split()) if i*18-9 < phi][-1]
    c = [c for c in C if c[0]/2 < r][-1][1]
    return c + ['',p][c in ('','D','T')]
