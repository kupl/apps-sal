def get_face(face):
    faces = { ':D':0, ':)':1, ':|':2, ':(':3, 'T_T':4 }
    return faces[face]

def sort_emotions(arr, order):
    return sorted(arr, key=get_face, reverse= not order)

