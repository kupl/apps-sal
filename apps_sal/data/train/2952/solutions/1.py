def dropzone(p, dropzones):
    return min(dropzones, key=lambda q: (q[0] - p[0])**2 + (q[1] - p[1])**2)
