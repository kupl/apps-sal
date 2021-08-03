def dropzone(p, dropzones):
    return min(dropzones, key=lambda d: (((d[0] - p[0])**2 + (d[1] - p[1])**2)**0.5, (d[0]**2 + d[1]**2)**0.5))
