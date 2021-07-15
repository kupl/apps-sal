def word_mesh(arr):
    result = ""
    
    for a, b in zip(arr, arr[1:]):
        while not a.endswith(b):
            b = b[:-1]
        if not b:
            return "failed to mesh"
        result += b
      
    return result
