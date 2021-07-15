def colour_association(arr):
    result = []
    for association in arr:
        colour, value = association
        result.append({colour : value})
    return result
