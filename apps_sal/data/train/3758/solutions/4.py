def word_mesh(lst):
    meshes = []
    for (w1, w2) in zip(lst, lst[1:]):
        for i in range(min(len(w1), len(w2)), 0, -1):
            if w1[-i:] == w2[:i]:
                meshes.append(w1[-i:])
                break
        else:
            return 'failed to mesh'
    return ''.join(meshes)
