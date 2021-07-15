def dropzone(p, dropzones):
    distances = []
    for dropzone in dropzones:
        distances.append(((dropzone[0]-p[0])**2+(dropzone[1]-p[1])**2)**0.5)
    return dropzones[distances.index(min(distances))]
