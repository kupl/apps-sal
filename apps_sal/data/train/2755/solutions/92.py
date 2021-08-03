def multiple_of_index(arr):
    listofmultiples = []
    index = 0
    for eachnumber in arr:
        if index == 0:
            index = index + 1
        elif eachnumber % index == 0:
            listofmultiples.append(eachnumber)
            index = index + 1
        else:
            index = index + 1
    return listofmultiples
