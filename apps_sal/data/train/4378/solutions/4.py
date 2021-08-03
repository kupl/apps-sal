def find_spaceship(astromap):
    arr = astromap.split('\n')[::-1]
    for i in range(len(arr)):
        print(arr[i])
        for j in range(len(arr[i])):
            if arr[i][j] == 'X':
                return [j, i]
    return "Spaceship lost forever."
