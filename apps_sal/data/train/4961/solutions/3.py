def box(coords):
    return {'nw': [max((i[0] for i in coords)), min((i[1] for i in coords))], 'se': [min((i[0] for i in coords)), max((i[1] for i in coords))]}
