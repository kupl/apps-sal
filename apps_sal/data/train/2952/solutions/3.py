def dropzone(p, dropzones):
    return min(dropzones, key=lambda d: (p[0]-d[0])**2 + (p[1]-d[1])**2)
