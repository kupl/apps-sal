import numpy as np

def determinant(a):
    return round(np.linalg.det(np.matrix(a)))

f = lambda x: x + [1]

def on_line(points =None):
    if points == None: return True
    if len(points) <= 2: return True
    points = map(list,list(points))
    for i in range(len(points)-2):
        matrix = [points[i], points[i+1], points[i+2]]
        matrix = map(f,matrix)
        if determinant(matrix) != 0:return False
    return True
