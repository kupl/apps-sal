def cube_odd(arr):

    sol = 0

    for i in arr:

        if type(i) != int:
            break

        elif i % 2:
            sol += i**3

    else:
        return sol
