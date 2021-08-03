def solve(arr, reach):
    dogs, nCats = {i for i, x in enumerate(arr) if x == 'D'}, 0
    for i, c in enumerate(arr):
        if c == 'C':
            catchingDog = next((i + id for id in range(-reach, reach + 1) if i + id in dogs), None)
            if catchingDog is not None:
                nCats += 1
                dogs.remove(catchingDog)
    return nCats
